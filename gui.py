import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Uncomment and run once if you haven't downloaded these
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')

prefixes = {
    "un": "not, opposite of",
    "re": "again",
    "dis": "not, opposite of",
    "pre": "before",
    "in": "not or into",
    "im": "not or into",
    "inter": "between",
    "mis": "wrongly",
    "sub": "under, below",
    "super": "above, beyond",
    "trans": "across, beyond",
    "anti": "against",
    "auto": "self",
    "bi": "two",
    "circum": "around",
    "de": "down, away, reverse",
    "ex": "out of, former",
    "fore": "before",
    "mid": "middle",
    "over": "excessive",
    "semi": "half",
    "under": "below, insufficient",
}

suffixes = {
    "ing": "action or process",
    "ness": "state or quality",
    "ed": "past tense",
    "er": "one who, comparative",
    "ly": "characteristic of",
    "tion": "state or action",
    "ity": "state or quality",
    "ment": "action or process",
    "able": "capable of being",
    "al": "pertaining to",
    "ence": "state or quality",
    "est": "superlative adjective",
    "ful": "full of",
    "ic": "pertaining to",
    "ish": "like, characteristic of",
    "let": "small",
    "ous": "full of",
    "ship": "state or condition",
    "y": "characterized by",
}

prefix_types = {
    "un": ("bound morpheme", "derivational (negation)"),
    "re": ("bound morpheme", "derivational (repetition)"),
    "dis": ("bound morpheme", "derivational (negation)"),
    "pre": ("bound morpheme", "derivational (temporal: before)"),
    "in": ("bound morpheme", "derivational (negation or direction)"),
    "im": ("bound morpheme", "derivational (negation or direction)"),
    "inter": ("bound morpheme", "derivational (between)"),
    "mis": ("bound morpheme", "derivational (wrongly)"),
    "sub": ("bound morpheme", "derivational (spatial: under, below)"),
    "super": ("bound morpheme", "derivational (spatial: above, beyond)"),
    "trans": ("bound morpheme", "derivational (across, beyond)"),
    "anti": ("bound morpheme", "derivational (against)"),
    "auto": ("bound morpheme", "derivational (self)"),
    "bi": ("bound morpheme", "derivational (two)"),
    "circum": ("bound morpheme", "derivational (around)"),
    "de": ("bound morpheme", "derivational (down, away, reverse)"),
    "ex": ("bound morpheme", "derivational (out of, former)"),
    "fore": ("bound morpheme", "derivational (temporal: before)"),
    "mid": ("bound morpheme", "derivational (spatial: middle)"),
    "over": ("bound morpheme", "derivational (excessive)"),
    "semi": ("bound morpheme", "derivational (half)"),
    "under": ("bound morpheme", "derivational (below, insufficient)"),
}

suffix_types = {
    "ing": ("bound morpheme", "inflectional (progressive verb form)"),
    "ness": ("bound morpheme", "derivational (forms nouns from adjectives)"),
    "ed": ("bound morpheme", "inflectional (past tense of verbs)"),
    "er": ("bound morpheme", "derivational (agent noun or comparative adjective)"),
    "ly": ("bound morpheme", "derivational (forms adverbs from adjectives)"),
    "tion": ("bound morpheme", "derivational (forms nouns)"),
    "ity": ("bound morpheme", "derivational (forms nouns)"),
    "ment": ("bound morpheme", "derivational (forms nouns)"),
    "able": ("bound morpheme", "derivational (capable of being)"),
    "al": ("bound morpheme", "derivational (pertaining to)"),
    "ence": ("bound morpheme", "derivational (state or quality)"),
    "est": ("bound morpheme", "inflectional (superlative adjective)"),
    "ful": ("bound morpheme", "derivational (full of)"),
    "ic": ("bound morpheme", "derivational (pertaining to)"),
    "ish": ("bound morpheme", "derivational (like, characteristic of)"),
    "let": ("bound morpheme", "derivational (small)"),
    "ous": ("bound morpheme", "derivational (full of)"),
    "ship": ("bound morpheme", "derivational (state or condition)"),
    "y": ("bound morpheme", "derivational (characterized by)"),
}

lemmatizer = WordNetLemmatizer()

def is_real_word(word):
    return bool(wordnet.synsets(word))

def analyze_word(word):
    word = word.lower()
    found_prefix = ""
    found_suffix = ""
    root_candidate = word

    for p in sorted(prefixes, key=len, reverse=True):
        if word.startswith(p):
            maybe_root = word[len(p):]
            if is_real_word(maybe_root):
                found_prefix = p
                root_candidate = maybe_root
                break

    for s in sorted(suffixes, key=len, reverse=True):
        if root_candidate.endswith(s):
            maybe_root = root_candidate[:-len(s)]
            if is_real_word(maybe_root):
                found_suffix = s
                root_candidate = maybe_root
                break

    root_lemma = lemmatizer.lemmatize(root_candidate)

    if is_real_word(root_lemma):
        root_meaning = wordnet.synsets(root_lemma)[0].definition()
    else:
        root_meaning = "Not found in WordNet"

    lines = []
    lines.append(f"Results for: {word}")
    if found_prefix:
        p_type = prefix_types.get(found_prefix, ("unknown", "unknown"))
        lines.append(f"Prefix: {found_prefix} | Meaning: {prefixes[found_prefix]} | Type: {p_type[0]}, {p_type[1]} morpheme")
    lines.append(f"Root: {root_lemma} | Meaning: {root_meaning} | Type: free root morpheme")
    if found_suffix:
        s_type = suffix_types.get(found_suffix, ("unknown", "unknown"))
        lines.append(f"Suffix: {found_suffix} | Meaning: {suffixes[found_suffix]} | Type: {s_type[0]}, {s_type[1]} morpheme")
    if not (found_prefix or found_suffix):
        lines.append("No prefix or suffix found. The whole word may be the root.")
    return "\n".join(lines), found_prefix, found_suffix, root_lemma

def print_morpheme_tree_branch(word, found_prefix, found_suffix, root_lemma):
    word = word.lower()
    tree_lines = ["\nMorpheme Tree:"]
    if found_prefix and found_suffix:
        branch_line = "    /    |    \\"
        children_line = f"{found_prefix.center(5)}{root_lemma.center(10)}{found_suffix.center(4)}"
        tree_lines.append("    " + word)
        tree_lines.append(branch_line)
        tree_lines.append(children_line)
    elif found_prefix:
        tree_lines.append(word.center(16))
        tree_lines.append("     /   |")
        tree_lines.append("    /    |")
        tree_lines.append(f"{found_prefix.ljust(5)}{root_lemma.rjust(7)}")
    elif found_suffix:
        tree_lines.append(word.center(18))
        tree_lines.append("     |    \\")
        tree_lines.append("     |      \\")
        tree_lines.append(f"   {root_lemma.ljust(8)}{found_suffix.rjust(5)}")
    else:
        tree_lines.append("      " + root_lemma)
        tree_lines.append("    /   |   \\")
        tree_lines.append(f"  {'...'.center(2)}{root_lemma.center(8)}{'...'.center(8)}")
    return "\n".join(tree_lines)

# --- GUI functions ---

def analyze_and_display():
    word = entry.get().strip()
    if not word.isalpha():
        set_texts("Please enter only alphabetic characters.", "", clear_tree=True)
        return
    try:
        analysis, prefix, suffix, root = analyze_word(word)
        tree = print_morpheme_tree_branch(word, prefix, suffix, root)
        set_texts(analysis, tree)
    except Exception as e:
        set_texts(f"Error during analysis: {e}", "", clear_tree=True)

def set_texts(analysis_text, tree_text, clear_tree=False):
    analysis_output.config(state="normal")
    analysis_output.delete(1.0, tk.END)
    analysis_output.insert(tk.END, analysis_text)
    analysis_output.config(state="disabled")

    tree_output.config(state="normal")
    if clear_tree:
        tree_output.delete(1.0, tk.END)
    else:
        tree_output.delete(1.0, tk.END)
        tree_output.insert(tk.END, tree_text)
    tree_output.config(state="disabled")

def refresh_fields():
    entry.delete(0, tk.END)
    set_texts("", "", clear_tree=True)
    entry.focus()

def save_output():
    # Combine analysis and tree outputs for saving
    analysis_text = analysis_output.get(1.0, tk.END).strip()
    tree_text = tree_output.get(1.0, tk.END).strip()

    if not analysis_text and not tree_text:
        messagebox.showinfo("Save Output", "Nothing to save. Please analyze a word first.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        title="Save analysis output as..."
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(analysis_text + "\n\n" + tree_text)
            messagebox.showinfo("Save Output", f"Output successfully saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save the file:\n{e}")

def show_help():
    help_text = (
        "Morpheme Analyzer Help:\n\n"
        "- Enter a single English word in the input box.\n"
        "- Click 'Analyze' to see morpheme analysis and the morpheme tree.\n"
        "- Use 'Refresh' to clear all fields and input a new word.\n"
        "- Use File > Save to save the current output to a text file.\n"
        "- Use File > Exit to close the application.\n"
    )
    messagebox.showinfo("Help - Morpheme Analyzer", help_text)

def exit_app():
    root.quit()

# --- Setup the main window ---

root = tk.Tk()
root.title("Morpheme Analyzer")

# Menu bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Save", command=save_output)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# Input label and entry
tk.Label(root, text="Enter a word to analyze:").pack(padx=10, pady=5)

entry = tk.Entry(root, width=24, font=("Arial", 14))
entry.pack(padx=10, pady=5)
entry.focus()

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(padx=10, pady=5)

analyze_btn = tk.Button(btn_frame, text="Analyze", command=analyze_and_display)
analyze_btn.pack(side=tk.LEFT, padx=5)

refresh_btn = tk.Button(btn_frame, text="Refresh", command=refresh_fields)
refresh_btn.pack(side=tk.LEFT, padx=5)

# Analysis output
tk.Label(root, text="Analysis Result:").pack(padx=10, pady=(10, 0))
analysis_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=8, font=("Consolas", 11))
analysis_output.pack(padx=10, pady=5)
analysis_output.config(state="disabled")

# Morpheme tree output
tk.Label(root, text="Morpheme Tree:").pack(padx=10, pady=(10, 0))
tree_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=6, font=("Consolas", 11))
tree_output.pack(padx=10, pady=5)
tree_output.config(state="disabled")

root.mainloop()
