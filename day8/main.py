#Day 8 — Caesar Cipher

# ✅ PROJECT: Caesar Cipher
# 1) Build a list of letters (a–z); optionally support uppercase
# 2) Ask for direction: 'encode' or 'decode'; ask for message and shift number
# 3) Normalize message (lowercase) but preserve spaces/punctuation
# 4) Use modulo arithmetic: new_index = (index ± shift) % 26 depending on direction
# 5) Reconstruct the transformed string; print the result
# 6) (Edge) Handle shift values > 26 or negative by normalizing with % 26
# 7) (Loop) After finishing, ask user if they want another go
# 8) (Polish) Preserve original casing; skip transforming non-letters cleanly