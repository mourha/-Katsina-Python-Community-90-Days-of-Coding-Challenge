
#Day 7 — Hangman

# ✅ PROJECT: Hangman
# 1) Prepare a word list; randomly choose a secret word
# 2) Create a display list of underscores matching the secret word length
# 3) Track lives (e.g., 6) and guessed letters (set to avoid duplicates)
# 4) Loop: ask for a letter; normalize to lowercase; validate single alphabetic char
# 5) If guessed before, warn and continue; don’t penalize twice
# 6) If letter in word: reveal all positions in display
# 7) Else: decrement lives and show hangman stage ASCII
# 8) End conditions: all letters revealed (win) OR lives == 0 (lose)
# 9) Reveal the answer on loss; ask to play again (loop)
# 10) (Polish) Draw the word progress with spaces; avoid flicker; add difficulty levels