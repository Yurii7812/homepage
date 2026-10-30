// 3x3x3 キューブの状態と 8 バイトの文字列を相互に変換する。
// 面の順（色の番号）: 0=U(白) 1=R(赤) 2=F(緑) 3=D(黄) 4=L(橙) 5=B(青)
// 状態は 54 枚のシールの色（0〜5）の配列。シールの番号は 面*9 + 行*3 + 列。

const FACES = [
  { n: [0, 1, 0], right: [1, 0, 0], up: [0, 0, -1] }, // U
  { n: [1, 0, 0], right: [0, 0, -1], up: [0, 1, 0] }, // R
  { n: [0, 0, 1], right: [1, 0, 0], up: [0, 1, 0] }, // F
  { n: [0, -1, 0], right: [1, 0, 0], up: [0, 0, 1] }, // D
  { n: [-1, 0, 0], right: [0, 0, 1], up: [0, 1, 0] }, // L
  { n: [0, 0, -1], right: [-1, 0, 0], up: [0, 1, 0] }, // B
];

const key = (v) => v.join(',');
const add = (a, b) => a.map((x, i) => x + b[i]);
const scale = (a, k) => a.map((x) => x * k);
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const cross = (a, b) => [
  a[1] * b[2] - a[2] * b[1],
  a[2] * b[0] - a[0] * b[2],
  a[0] * b[1] - a[1] * b[0],
];
// 軸 a の周りに 90 度回す
const turn = (v, a) => add(cross(a, v), scale(a, dot(a, v)));

// シールの位置（キューブの小片の座標）と向き（外向きの法線）
const STICKERS = [];
const STICKER_INDEX = new Map();
FACES.forEach((face, f) => {
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      const pos = add(add(face.n, scale(face.right, c - 1)), scale(face.up, 1 - r));
      const idx = f * 9 + r * 3 + c;
      STICKERS[idx] = { pos, n: face.n };
      STICKER_INDEX.set(key(pos) + '|' + key(face.n), idx);
    }
  }
});

// 位置と向きからシールの番号を引く
export function stickerIndex(pos, n) {
  return STICKER_INDEX.get(key(pos) + '|' + key(n));
}
export const STICKER_POSITIONS = STICKERS;

// 面の法線から色の番号
const colorOf = (n) => FACES.findIndex((face) => key(face.n) === key(n));

// 1 回転（90 度）の並べ替え表。perm[j] は、シール j が移動する先。
function quarterTurnPerm(f) {
  const a = FACES[f].n;
  const perm = STICKERS.map((_, j) => j);
  STICKERS.forEach((s, j) => {
    if (dot(s.pos, a) === 1) {
      perm[j] = stickerIndex(turn(s.pos, a), turn(s.n, a));
    }
  });
  return perm;
}
const QUARTER = FACES.map((_, f) => quarterTurnPerm(f));
const MOVE_FACE = { U: 0, R: 1, F: 2, D: 3, L: 4, B: 5 };

// 手順（例 "R U' F2"）を状態に適用する
export function applyMoves(colors, moves) {
  let cur = colors.slice();
  for (const m of moves.trim().split(/\s+/).filter(Boolean)) {
    const face = MOVE_FACE[m[0]];
    if (face === undefined) throw new Error('不明な手: ' + m);
    const times = m[1] === "'" ? 3 : m[1] === '2' ? 2 : 1;
    for (let t = 0; t < times; t++) {
      const next = cur.slice();
      QUARTER[face].forEach((to, j) => {
        next[to] = cur[j];
      });
      cur = next;
    }
  }
  return cur;
}

// 角・辺のピース（家の位置）と、そのシールの並び
const CORNERS = [];
const EDGES = [];
for (const sx of [-1, 1]) {
  for (const sy of [-1, 1]) {
    for (const sz of [-1, 1]) CORNERS.push([sx, sy, sz]);
  }
}
for (let x = -1; x <= 1; x++) {
  for (let y = -1; y <= 1; y++) {
    for (let z = -1; z <= 1; z++) {
      const nonzero = [x, y, z].filter((v) => v !== 0).length;
      if (nonzero === 2) EDGES.push([x, y, z]);
    }
  }
}

// 角: 3 枚のシールを、手前から見て同じ向き（右手系）に並べる。
// 角の 3 枚の向きは x, y, z 軸のどれかになる。
function cornerNormals(pos) {
  const [x, y, z] = pos;
  const nx = [x, 0, 0];
  const ny = [0, y, 0];
  const nz = [0, 0, z];
  return x * y * z > 0 ? [nx, ny, nz] : [nx, nz, ny];
}
// 基準（上下の面 = y 軸）が先頭になるように並べ替える
function refFirst(list, isRef) {
  const i = list.findIndex(isRef);
  return [...list.slice(i), ...list.slice(0, i)];
}
const isY = (v) => v[1] !== 0;

// 辺: 上下の面（y 軸）があればそれを基準、無ければ前後（z 軸）を基準にする
function edgeNormals(pos) {
  const parts = [];
  if (pos[0] !== 0) parts.push([pos[0], 0, 0]);
  if (pos[1] !== 0) parts.push([0, pos[1], 0]);
  if (pos[2] !== 0) parts.push([0, 0, pos[2]]);
  return parts;
}

const CORNER_CYC = CORNERS.map((pos) => refFirst(cornerNormals(pos), isY));
const EDGE_CYC = EDGES.map((pos) => {
  const parts = edgeNormals(pos);
  const hasY = parts.some(isY);
  return refFirst(parts, hasY ? isY : (v) => v[2] !== 0);
});
const CORNER_SLOT_IDX = CORNERS.map((pos) => cornerNormals(pos).map((n) => stickerIndex(pos, n)));
const EDGE_SLOT_IDX = EDGES.map((pos, s) => EDGE_CYC[s].map((n) => stickerIndex(pos, n)));

// 同じ色の組み合わせのピースを探すための表
const colorSetKey = (cols) => [...cols].sort((a, b) => a - b).join(',');
const CORNER_KEY = new Map(CORNER_CYC.map((ns, k) => [colorSetKey(ns.map(colorOf)), k]));
const EDGE_KEY = new Map(EDGE_CYC.map((ns, k) => [colorSetKey(ns.map(colorOf)), k]));

// 順列
const FACT = [1];
for (let i = 1; i <= 12; i++) FACT[i] = FACT[i - 1] * i;

function unrankPerm(rank, n) {
  const avail = Array.from({ length: n }, (_, i) => i);
  const out = [];
  let r = rank;
  for (let i = n; i > 0; i--) {
    const f = FACT[i - 1];
    const q = Math.floor(r / f);
    r %= f;
    out.push(avail.splice(q, 1)[0]);
  }
  return out;
}
function rankPerm(perm) {
  const n = perm.length;
  const avail = Array.from({ length: n }, (_, i) => i);
  let rank = 0;
  for (let i = 0; i < n; i++) {
    const q = avail.indexOf(perm[i]);
    rank += q * FACT[n - 1 - i];
    avail.splice(q, 1);
  }
  return rank;
}
function parity(perm) {
  let inv = 0;
  for (let i = 0; i < perm.length; i++) {
    for (let j = i + 1; j < perm.length; j++) if (perm[i] > perm[j]) inv++;
  }
  return inv % 2;
}

// 角の順列（8 個）を偶奇ごとに、辞書順で並べた表
const CORNER_PERMS = [[], []];
const CORNER_PERM_INDEX = [new Map(), new Map()];
for (let r = 0; r < FACT[8]; r++) {
  const p = unrankPerm(r, 8);
  const par = parity(p);
  CORNER_PERM_INDEX[par].set(p.join(), CORNER_PERMS[par].length);
  CORNER_PERMS[par].push(p);
}

const TOTAL_EDGE_PERM = FACT[12]; // 479001600
const TOTAL_CORNER_PERM = CORNER_PERMS[0].length; // 20160（偶奇それぞれ）

// 8 バイトの文字列 ↔ 数（64 ビット）
const big = (n) => BigInt(n);
export function textToNumber(text) {
  const bytes = new TextEncoder().encode(text);
  if (bytes.length > 8) throw new Error('8バイトまでです（今: ' + bytes.length + 'バイト）');
  let n = 0n;
  for (let i = 0; i < 8; i++) n = (n << 8n) | big(i < bytes.length ? bytes[i] : 0);
  return n;
}
export function numberToText(n) {
  const bytes = [];
  let rest = n;
  for (let i = 0; i < 8; i++) {
    bytes.unshift(Number(rest & 255n));
    rest >>= 8n;
  }
  let end = bytes.length;
  while (end > 0 && bytes[end - 1] === 0) end--;
  return new TextDecoder().decode(new Uint8Array(bytes.slice(0, end)));
}

// 数（0 以上 2^64 未満）→ キューブの色
// 内訳: 辺の順列 12! × 角の順列 20160 × 角の向き 3^7 × 辺の向き 2^11
export function encodeNumber(N) {
  const e = Number(N % big(TOTAL_EDGE_PERM));
  let rest = N / big(TOTAL_EDGE_PERM);
  const c = Number(rest % big(TOTAL_CORNER_PERM));
  rest /= big(TOTAL_CORNER_PERM);
  let T = Number(rest % 2187n);
  const F = Number(rest / 2187n);
  if (F >= 2048) throw new Error('範囲外の値です');

  const edgePerm = unrankPerm(e, 12);
  const par = parity(edgePerm);
  const cornerPerm = CORNER_PERMS[par][c];

  const tw = [];
  for (let j = 0; j < 7; j++) {
    tw.push(T % 3);
    T = Math.floor(T / 3);
  }
  tw.push((3 - (tw.reduce((a, b) => a + b, 0) % 3)) % 3);
  const fl = [];
  let f = F;
  for (let j = 0; j < 11; j++) {
    fl.push(f % 2);
    f = Math.floor(f / 2);
  }
  fl.push(fl.reduce((a, b) => a + b, 0) % 2);

  const colors = new Array(54).fill(0);
  FACES.forEach((_, face) => {
    colors[face * 9 + 4] = face; // 中心のシール
  });
  for (let s = 0; s < 8; s++) {
    const cyc = CORNER_CYC[cornerPerm[s]];
    for (let i = 0; i < 3; i++) {
      colors[CORNER_SLOT_IDX[s][i]] = colorOf(cyc[(i - tw[s] + 3) % 3]);
    }
  }
  for (let s = 0; s < 12; s++) {
    const cyc = EDGE_CYC[edgePerm[s]];
    for (let i = 0; i < 2; i++) {
      colors[EDGE_SLOT_IDX[s][i]] = colorOf(cyc[(i - fl[s] + 2) % 2]);
    }
  }
  return colors;
}

// キューブの色 → 数。おかしい状態（組み合わせが不可能）なら例外。
export function decodeColors(colors) {
  const cornerPerm = [];
  const tw = [];
  for (let s = 0; s < 8; s++) {
    const cols = CORNER_SLOT_IDX[s].map((i) => colors[i]);
    const k = CORNER_KEY.get(colorSetKey(cols));
    if (k === undefined) throw new Error('角のピースが不正です');
    const cyc = CORNER_CYC[k].map(colorOf);
    const t = cols.indexOf(cyc[0]);
    if (t < 0) throw new Error('角の向きが不正です');
    for (let i = 0; i < 3; i++) {
      if (cols[(t + i) % 3] !== cyc[i]) throw new Error('角の並びが不正です');
    }
    cornerPerm.push(k);
    tw.push(t);
  }
  const edgePerm = [];
  const fl = [];
  for (let s = 0; s < 12; s++) {
    const cols = EDGE_SLOT_IDX[s].map((i) => colors[i]);
    const k = EDGE_KEY.get(colorSetKey(cols));
    if (k === undefined) throw new Error('辺のピースが不正です');
    const cyc = EDGE_CYC[k].map(colorOf);
    const f = cols.indexOf(cyc[0]);
    if (f < 0) throw new Error('辺の向きが不正です');
    if (cols[(f + 1) % 2] !== cyc[1]) throw new Error('辺の並びが不正です');
    edgePerm.push(k);
    fl.push(f);
  }
  if (new Set(cornerPerm).size !== 8 || new Set(edgePerm).size !== 12) {
    throw new Error('同じピースが重なっています');
  }
  const par = parity(edgePerm);
  if (parity(cornerPerm) !== par) throw new Error('組み合わせが不可能です（偶奇が合いません）');
  if (tw.reduce((a, b) => a + b, 0) % 3 !== 0) throw new Error('角の向きの合計が不正です');
  if (fl.reduce((a, b) => a + b, 0) % 2 !== 0) throw new Error('辺の向きの合計が不正です');

  const c = CORNER_PERM_INDEX[par].get(cornerPerm.join());
  let T = 0;
  for (let j = 6; j >= 0; j--) T = T * 3 + tw[j];
  let F = 0;
  for (let j = 10; j >= 0; j--) F = F * 2 + fl[j];
  return (
    big(rankPerm(edgePerm)) +
    big(TOTAL_EDGE_PERM) * (big(c) + big(TOTAL_CORNER_PERM) * (big(T) + 2187n * big(F)))
  );
}

export function textToColors(text) {
  return encodeNumber(textToNumber(text));
}
export function colorsToText(colors) {
  return numberToText(decodeColors(colors));
}
export const SOLVED = encodeNumber(0n);
