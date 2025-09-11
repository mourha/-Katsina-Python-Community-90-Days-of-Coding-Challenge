#Day 5 — Password Generator

# ✅ PROJECT: Password Generator
# 1) Define pools: letters (a-z, A-Z), numbers (0-9), symbols (!@#$%^&* etc.)
# 2) Ask how many letters, numbers, and symbols the user wants
# 3) Validate inputs (non-negative ints); re-prompt on invalid
# 4) Randomly pick requested counts from each pool
# 5) Combine selections into a list; shuffle -> random.shuffle()
# 6) Join into a final password string; print to the user
# 7) (Edge) If total length < 4, warn that it’s weak
# 8) (Polish) Offer “simple” vs “strong” presets; measure entropy approx by length/classes