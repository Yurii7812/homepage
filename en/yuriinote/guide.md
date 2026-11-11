# YuriiNote illustrated user manual

Based on YuriiNote 1.1.0 and the development branch below. Major workflows were checked in Electron using sample data. Screenshots show the Japanese UI; English instructions identify the corresponding controls.

Development version: unified Index, expanded display filtering, Topic Index completion and marker changes belong to the working branch. A source change is separate from a merged stable release or published installer.


## 1. Installation, first launch and vault

A vault is an ordinary folder containing your notes, indexes and images.

1. Find a file for your OS on <a href="https://github.com/Yurii7812/YuriiNote/releases">Releases</a>: Windows installer, macOS DMG or Linux AppImage. A released binary may not include changes from the development branch.
2. To try the development source, check out the specified GitHub branch. With Node.js and npm installed, run <code>npm ci</code>, <code>npm run build</code>, then <code>npm start</code> in the repository.
3. On first launch, choose the folder option to open an existing vault or select a new location. You can also open a detected vault from the listed candidates.
4. After launch, open ⚙️ Settings at the lower left, find Vault and press Change. Pending saves finish before switching folders.
5. Select Japanese or English under Language. Adjust the interface scale and body text size if necessary.

## 2. Layout, tabs and save status

Use the vertical rail to select a feature, open an item from the left list, and work in the center. Related information appears on the right.

1. The rail opens Notes 📝, Diary 📔, Chat memos 💬, unified Index 🗂, Graph 🕸, Mandala ❖ and Cards 🗒.
2. Click a note in the left list to open it. Follow Keywords, Own topic, Topics, Parent, Children and Backlinks in the right column.
3. Use the top plus button for the creation menu, the search box to search, and the arrow buttons for navigation history.
4. Ctrl+T opens an empty tab; Ctrl+W closes a tab. Ctrl+Tab / Ctrl+Shift+Tab switches tabs. Middle-click a reference to open it in a background tab.
5. After editing, wait for Saving to become Saved. Click a save-error status to retry.

Screenshots use the Japanese UI. An out-of-scope editor remains mounted so its draft and undo history are retained.

## 3. Create and edit an unnumbered note

Write first and organize later. Title and body are separate editable fields.

1. In the Notes view, press the top-right plus and choose 📝 Note. An unnumbered note opens.
2. Click Title to enter a title. Click the body and write prose or Markdown.
3. Use headings, lists and checkboxes. The Table button inserts a table template.
4. Ctrl+Z undoes a body edit; Ctrl+Shift+Z or Ctrl+Y redoes it. Check the save status when moving to another note.
5. Find unnumbered notes under Inbox / Unorganized (📥). You can keep writing before assigning an ID.

## 4. Assign, change, branch and create sibling IDs

Paper and digital IDs use independent namespaces. Paper 1a and digital 1a are different notes.

1. Press Assign ID at the top of an unnumbered note. In the ID explorer, search and select a reference position.
2. Choose direct assignment, branch or sibling, check the proposed ID and namespace, then confirm. Keep paper and digital IDs distinct.
3. On a numbered note, + Branch creates a child and + Sibling creates the next item at that level. Branch examples: 1 → 1a → 1a1. A sibling of 1a is 1b.
4. Click the displayed ID to copy it. To change or clear it, use the note’s ⋯ menu and the explicit Change / clear ID action.
5. Follow Parent and Children in the right panel. Notes containing references to this note appear in its backlinks.

Choose placement from the relationship between ideas. Do not deepen the ID merely because a page comes next.

## 5. Global display filter

This display setting is independent of the search query. It does not delete or move source data.

1. Open Display filter at the upper left.
2. Choose All, Paper only or Digital only. If a shared keyword has 1a(p) and 1a(d), Paper only shows just 1a(p).
3. Check the Index, Topic Index references, search candidates, relationships, backlinks, similar notes, graph, cards and mandala. View-specific filters still narrow the result further.
4. If the active note is excluded, its editor is hidden while keeping the draft. Switch back to restore it. The Topic Index editor works with the full source text that will be saved.
5. The selection is restored after restart. Chat memos, ordinary diary prose and standalone files are digital. In paper-only diary view, only the imported paper diary images are shown; digital prose stays preserved and hidden.

## 6. Register keywords, readings and IDs in the unified Index

Look up paper and digital IDs by keyword, including paper IDs that have not been scanned.

1. Open the unified Index using 🗂 in the rail or the Index (🔖) tab. Keywords are grouped in Japanese reading order.
2. Press + above the list. Enter Keyword and Reading; correct an automatically suggested reading if necessary.
3. Search notes by title, ID or body, then click a candidate to add its ID. Candidates identify paper or digital.
4. You may also type IDs in Associated IDs. Enter an unscanned paper ID as <code>9a(p)</code> and an existing digital ID as <code>1(d)</code>, separated by spaces. An omitted namespace means paper.
5. Check the neighboring-keyword preview and press Save. The reading and IDs appear in the unified Index.
6. Right-click the keyword text and choose Edit Index to change the name, reading or IDs. Remove keyword unregisters the index association while keeping the notes.
7. Click a keyword label in search results to clear the query and locate that keyword among its neighbors in the unified Index.

## 7. Create a Topic Index and select markers

The global Index gives entry points across the collection; a Topic Index organizes references within a subject.

1. Open a numbered note and press + beside Topics in the right column.
2. Search for an existing index, or use the plus beside the name field to enter a new index name. Check its entry ID and namespace.
3. Open the index and press Edit. Write a keyword and IDs on each line, such as <code>Coffee 1a 2(p)</code>. An unqualified ID uses the namespace of the index entry.
4. Type <code>^</code>, <code>+</code> or <code>=</code> at the start of a line. Alternatively place the cursor on the line, choose Reference type and press Apply to current line.
5. Press Done to return to the rendered view and check ↑, ★ and ●. Name / entry lets you inspect or change the name and entry.

A red dot above an ID indicates an associated Topic Index. It is different from a leading ● for summary / progress. One ID has one Topic Index; identical paper and digital IDs remain separate.

## 8. Add a Topic Index item with colon search

Completion uses a keyword–ID row in an index and a reference link in ordinary prose.

1. Open the Topic Index and press Edit. Make a new line at the intended insertion point.
2. Type an ASCII <code>:</code>. Continue with a title or ID query to narrow the candidates.
3. Check the title, ID and paper/digital label. Use Up/Down and Enter, or click a candidate.
4. The index receives a row such as <code>Paper thinking 1(p)</code>, rather than the ordinary prose link <code>:1(p)</code>.
5. Apply a marker to the line if needed. Escape cancels completion and leaves the typed text. Undo / Redo reverses or reapplies the insertion.
6. Press Done and check the row and its target. With Paper only selected, completion offers paper notes only.

## 9. Prose references, search and backlinks

Global search and inline reference completion are different actions. Ordinary-note completion retains the existing link syntax.

1. Type in the top search box. Results are grouped as global Index, Topic Index and notes. Escape clears/exits search.
2. In prose, type <code>:</code>, enter a query and choose a candidate. Enter inserts a prefix reference; Shift+Enter inserts a postfix reference.
3. When typing manually, <code>:1a</code> points to a continuation, <code>1a:</code> introduces a source note, and <code>1a(1)</code> identifies a numbered passage. Use <code>:1a(p)</code> for paper or <code>:1a(d)</code> for digital explicitly.
4. Mark a passage with <code>(1)</code> and use <code>(1):</code> to comment on that passage in the same note. Click a link to navigate and use Back to return.
5. In the target note’s Backlinks panel, read referring notes and their context. Use ≈ Similar notes to find related material too.

## 10. Paper notes, scans and unscanned IDs

Import paper notes using their physical IDs. The Index can locate physical notes before a scan exists.

1. In the Notes view, choose Plus → Import scan (paper), then select image files.
2. Review the image in the scan screen, enter the paper ID and optional keywords, and register it. An existing ID in the paper namespace is rejected as a duplicate.
3. Open the note from the Paper (📜) tab. Its image and an editable text area appear. Add a title or searchable transcription.
4. Choose Display filter → Paper only, then use the Index or search to locate the paper ID. An ID without a scanned note appears as a missing/placeholder reference.
5. Before scanning, register an ID such as <code>9a(p)</code> through + in the unified Index. A later scan with that paper ID connects to it.
6. For a paper diary, choose a date in the scan screen and import it as Diary. The image goes into that day’s diary rather than receiving a Folgezettel ID.

Paper diary images are stored inside diary records. Open the diary with Paper only selected to view just the scanned pages. These are dated records, separate from Folgezettel paper notes.

## 11. Chat memos: send, organize and edit

Capture short messages as bubbles and organize them into notes later.

1. Click 💬 in the rail and select a topic. To create one, press + above the topic list, enter a name, then Create or Enter.
2. Write in the bottom input and press Enter to send. Shift+Enter inserts a newline. Enter used to confirm IME composition does not send the message.
3. Click a different topic in the list to switch. Use the bottom 💬 control and Create child topic to branch the topic context; subsequent posts inherit its upper-topic settings.
4. Right-click a bubble and choose Edit. Enter finishes editing; Escape cancels.
5. Use ↩ on a bubble to choose a reply target, then write and send. Use ⇆ to edit existing reply targets. Colon search or @ can add references/mentions to notes and memos.
6. Use 📎 at the bottom right or drag files into the chat. Open an attachment through its message link.

## 12. Select chat memos, make notes and connect diaries

Making a note keeps the original memos and creates an ordinary editable note that refers to them.

1. Choose ⋮ → Multiple selection at the top right of a chat, then select bubbles. Right-click → Select also starts selection.
2. Press Make note in the selection bar, inspect the title and destination settings, then create it. For one memo, use its right-click Make note action.
3. Add your own prose to the new ordinary note. Expanded source memos follow edits to their originals. A 📝 chip on a source bubble opens the resulting note.
4. Create link can group multiple notes/memos with a title, order and selected source range. A live reference is different from copying source text.
5. Posting to Diary or a record-type topic also adds timestamped content to that day’s record. Use ⋮ → By day to inspect a specific date.

## 13. Today, past diaries, dreams and work records

Diary entries are organized by date and record type, separately from Folgezettel notes.

1. Click 📔, then Today’s diary to open today’s entry.
2. For another day, enter a date on the left and press Open, or click an existing date. The ← / → buttons in the entry move between days.
3. The title is optional. Write in the body and check save status. Today’s notes links to notes created on that day.
4. Use + ⚙ beside the record types to create and organize types such as Dreams or Work. Configure parent relationships, including multiple upper record types.
5. Select a record type, then open its date. The day boundary is configurable in Settings and defaults to 05:00.
6. To import a paper diary image, use the scan workflow, select its date and register it as a diary. Read the image under Paper diary in the entry.

## 14. Roleplay, characters, replies and quotations

Characters are integrated into chat memos in the current implementation. The old “Plus → Roleplay chat” creation path is absent from the current menu.

1. Open a chat with 💬, then choose ⋮ → Character manager.
2. Enter a name in New character and press Save. Rename existing characters or hide them from the list in the same dialog.
3. Choose the character in the Display / posting character selector inside ⋮, then post from the input. Change that selector to write as another role.
4. Reply with ↩ and reference another utterance or note using @ or colon search. Check the source along with quoted text.
5. Legacy roleplay data is preserved during migration into chat. A directly opened legacy note can still show the old dedicated Quote button and role switcher. Keep those legacy controls separate from the current chat workflow.

## 15. Place cards and connections on a canvas

A canvas is a note type and can begin without a Folgezettel ID.

1. In Notes, choose Plus → Canvas, then enter a title.
2. Click an empty area of the dotted board and enter text. Click outside the field to finish editing.
3. Select a box, press ↗ Line and click the destination box. Drag boxes to move them.
4. Use + Note to search and embed a note, or + Image to add an image.
5. Double-click a line to label it. Zoom using Ctrl+wheel or + / −; Fit shows the whole board.
6. Select a box or line and press Delete to remove it. Escape cancels selection or connection mode.

## 16. Graph, cards, mandala and similar notes

Explore the same notes through relations, cards and similarity. Changing views does not change note IDs.

1. Open Graph with 🕸. Switch between the link map and tree map, and use ⚙️ to adjust visibility. Select a node to inspect it; double-click to open.
2. Graph options such as showing paper or orphan notes combine with the global display filter. Check both sets of filters if a note is missing.
3. Open Cards with 🗒. Click a card to edit in place; click outside or press Escape to close. Use its own type, search and sort controls too.
4. Open Mandala with ❖. Inspect a center note and its neighbors, then select items to navigate. Use 9×9 for a larger layout and Preview to read text.
5. Open a note, then press ≈ in the list toolbar, or s while not typing, to find Similar notes. Compare candidates using body, keywords, links and Topic Index criteria.

## 17. Attachments, bulk selection, export and recovery

Check the selected items before a bulk action. Export provides temporary Markdown for inspection and copying.

1. Use 📎 Attach on a note to select files, drag files onto the note, or paste an image. Images appear in the body; other files appear as links.
2. Use the Files (📎) tab to find imported files and add a title or description.
3. Press ☑ Select in the note list and select items. Use All, Copy, Create link or Similar notes. Escape or Cancel exits selection.
4. Choose Export, inspect the selection, optionally add related notes or an ID range, then Preview in temporary tab or Copy. Save a file yourself if needed.
5. Delete moves confirmed notes to .trash. To restore one, open Cards → 🗑 and press Restore on the item.
6. For a backup, copy the entire vault folder. A display filter is not a backup or migration operation.

## 18. Phone integration and app updates

Phone transfer uses USB and ADB. It is not a cloud synchronization workflow.

1. Enable USB debugging on the Android device and connect it by USB. ADB on the PC must recognize the device, and the phone must authorize the connection.
2. Choose Settings → Install phone app (USB) and follow the prompts. Availability of the companion APK depends on the distribution.
3. After recording on the phone, use the PC’s ⋯ → Import phone memos (USB), or enable automatic import in Settings.
4. Items are routed according to type, including unorganized memos, diary/record topics and numbered paper scans. Verify the actual imported content on your device.
5. Use Check for updates in Settings. Git, AppImage and installer distributions follow different update paths. Finish saving before proceeding with the displayed instructions.
6. To try an unmerged feature, explicitly check out its source branch. The update button does not automatically install an unmerged PR.

The screenshots and interactive checks used the development app on Linux. Windows/macOS installers, physical USB transfer and packaged self-updates were not exercised in this run.

## 19. Keyboard reference

Shortcuts depend on focus: text editor, list navigation and specialized views have different bindings.

1. Ctrl+F focuses search; Escape exits it.
2. Ctrl+N creates an unnumbered note. With a numbered note selected, Ctrl+B / Ctrl+H creates a branch / sibling.
3. In the editor use Ctrl+Z to undo and Ctrl+Shift+Z / Ctrl+Y to redo. In completion, use Up/Down, Enter and Escape.
4. When navigating the list, use Up/Down or j/k, and Left/Right or h/l. Use i to enter editing and s to open Similar notes.
5. Tab shortcuts are Ctrl+T, Ctrl+W and Ctrl+Tab. In chat input, Enter sends and Shift+Enter inserts a newline.

Prefer the visible menu/button when a shortcut is intercepted by the OS or IME.