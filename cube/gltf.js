// キューブの状態（シールの色 54 個）から、GLB（model-viewer で表示できる 3D ファイル）を作る。
import { stickerIndex } from './cube-core.js?v=3';

// 元の GLB と同じ色（白・赤・緑・黄・橙・青）と、黒っぽい本体の色
const STICKER_RGB = [
  [0.9529, 0.9529, 0.9216],
  [0.8588, 0.1569, 0.1843],
  [0.0941, 0.6039, 0.3647],
  [0.9647, 0.8039, 0.1294],
  [0.9373, 0.4706, 0.1059],
  [0.1216, 0.3529, 0.7922],
];
const BODY_RGB = [0.0706, 0.0784, 0.0941];
const DIRS = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]];

// 表示の色（見た目どおりの明るさ）を、glTF が使う直線の明るさに変換する
const toLinear = (rgb) => rgb.map((v) => (v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4));

// 軸 a の周りに角度 t だけ回す（右ねじの向き）
function rotateAxis(v, a, t) {
  const c = Math.cos(t);
  const s = Math.sin(t);
  const ad = a[0] * v[0] + a[1] * v[1] + a[2] * v[2];
  const ax = [a[1] * v[2] - a[2] * v[1], a[2] * v[0] - a[0] * v[2], a[0] * v[1] - a[1] * v[0]];
  return [0, 1, 2].map((i) => v[i] * c + ax[i] * s + a[i] * ad * (1 - c));
}

// 箱（中心 c、半径 h）を、面ごとに 4 頂点・2 三角形で追加する。
// rot があれば、頂点と法線をそれで回す（層を回した途中の形を作るため）。
function addBox(prim, c, h, rot = (v) => v) {
  for (let a = 0; a < 3; a++) {
    const b = (a + 1) % 3;
    const cc = (a + 2) % 3;
    for (const s of [1, -1]) {
      const corners = [[-1, -1], [1, -1], [1, 1], [-1, 1]];
      // 面の 4 頂点。s が負のときは向きを逆にして、外向きの面にする
      const order = s > 0 ? corners : [...corners].reverse();
      const base = prim.pos.length / 3;
      for (const [ub, uc] of order) {
        const p = [0, 0, 0];
        p[a] = c[a] + s * h[a];
        p[b] = c[b] + ub * h[b];
        p[cc] = c[cc] + uc * h[cc];
        prim.pos.push(...rot(p));
        const n = [0, 0, 0];
        n[a] = s;
        prim.nrm.push(...rot(n));
      }
      prim.idx.push(base, base + 1, base + 2, base, base + 2, base + 3);
    }
  }
}

const newPrim = () => ({ pos: [], nrm: [], idx: [] });

// colors（54 個）→ GLB のバイト列。
// turn があれば、その層（pos·axis = 1 の小片）を axis の周りに angle（ラジアン）回した形にする。
export function cubeGlb(colors, turn = null) {
  const body = newPrim();
  const stickers = STICKER_RGB.map(newPrim);
  const pieces = [];
  for (let x = -1; x <= 1; x++) {
    for (let y = -1; y <= 1; y++) {
      for (let z = -1; z <= 1; z++) {
        if (x === 0 && y === 0 && z === 0) continue;
        const pos = [x, y, z];
        const moving = turn && pos[0] * turn.axis[0] + pos[1] * turn.axis[1] + pos[2] * turn.axis[2] === 1;
        const rot = moving ? (v) => rotateAxis(v, turn.axis, turn.angle) : (v) => v;
        addBox(body, pos, [0.475, 0.475, 0.475], rot);
        for (const d of DIRS) {
          if (pos[0] * d[0] + pos[1] * d[1] + pos[2] * d[2] !== 1) continue;
          // シールは薄い板。法線の方向だけ薄くする
          const h = [0.4, 0.4, 0.4];
          const axis = d.findIndex((v) => v !== 0);
          h[axis] = 0.01;
          const c = pos.map((v, i) => v + d[i] * 0.485);
          addBox(stickers[colors[stickerIndex(pos, d)]], c, h, rot);
        }
      }
    }
  }
  pieces.push({ prim: body, rgb: BODY_RGB, rough: 0.82 });
  stickers.forEach((prim, i) => pieces.push({ prim, rgb: STICKER_RGB[i], rough: 0.43 }));
  return buildGlb(pieces.filter((p) => p.prim.idx.length > 0));
}

// 1 つの GLB に、材料ごとの図形をまとめる
function buildGlb(pieces) {
  const chunks = [];
  let byteLength = 0;
  const addView = (typed, target) => {
    const bytes = new Uint8Array(typed.buffer);
    const offset = byteLength;
    chunks.push(bytes);
    byteLength += bytes.byteLength;
    const pad = (4 - (byteLength % 4)) % 4;
    if (pad) {
      chunks.push(new Uint8Array(pad));
      byteLength += pad;
    }
    bufferViews.push({ buffer: 0, byteOffset: offset, byteLength: bytes.byteLength, target });
    return bufferViews.length - 1;
  };
  const bufferViews = [];
  const accessors = [];
  const addAccessor = (view, componentType, count, type, extra = {}) => {
    accessors.push({ bufferView: view, componentType, count, type, ...extra });
    return accessors.length - 1;
  };
  const primitives = pieces.map((piece, i) => {
    const { prim } = piece;
    const pos = new Float32Array(prim.pos);
    const nrm = new Float32Array(prim.nrm);
    const idx = new Uint16Array(prim.idx);
    const min = [0, 1, 2].map((k) => Math.min(...prim.pos.filter((_, j) => j % 3 === k)));
    const max = [0, 1, 2].map((k) => Math.max(...prim.pos.filter((_, j) => j % 3 === k)));
    const pv = addView(pos, 34962);
    const nv = addView(nrm, 34962);
    const iv = addView(idx, 34963);
    return {
      attributes: {
        POSITION: addAccessor(pv, 5126, pos.length / 3, 'VEC3', { min, max }),
        NORMAL: addAccessor(nv, 5126, nrm.length / 3, 'VEC3'),
      },
      indices: addAccessor(iv, 5123, idx.length, 'SCALAR'),
      material: i,
    };
  });
  const materials = pieces.map((piece) => ({
    pbrMetallicRoughness: {
      baseColorFactor: [...toLinear(piece.rgb), 1],
      roughnessFactor: piece.rough,
      metallicFactor: 0,
    },
    doubleSided: false,
  }));
  const json = {
    asset: { version: '2.0' },
    scene: 0,
    scenes: [{ nodes: [0] }],
    nodes: [{ mesh: 0 }],
    meshes: [{ primitives }],
    materials,
    accessors,
    bufferViews,
    buffers: [{ byteLength }],
  };
  let jsonBytes = new TextEncoder().encode(JSON.stringify(json));
  const jsonPad = (4 - (jsonBytes.length % 4)) % 4;
  jsonBytes = new Uint8Array([...jsonBytes, ...new Array(jsonPad).fill(0x20)]);
  const binLength = byteLength + ((4 - (byteLength % 4)) % 4);
  const total = 12 + 8 + jsonBytes.length + 8 + binLength;

  const out = new Uint8Array(total);
  const view = new DataView(out.buffer);
  view.setUint32(0, 0x46546c67, true); // "glTF"
  view.setUint32(4, 2, true);
  view.setUint32(8, total, true);
  view.setUint32(12, jsonBytes.length, true);
  view.setUint32(16, 0x4e4f534a, true); // "JSON"
  out.set(jsonBytes, 20);
  let off = 20 + jsonBytes.length;
  view.setUint32(off, binLength, true);
  view.setUint32(off + 4, 0x004e4942, true); // "BIN"
  off += 8;
  for (const c of chunks) {
    out.set(c, off);
    off += c.length;
  }
  return out;
}
