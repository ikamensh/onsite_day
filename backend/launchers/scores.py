from persistence import load_data, get_team
from score_calculator import average_score, synergy_score, onsite_score

load_data()

at = get_team(1)

fs = average_score(at)
gs = synergy_score(at)
scores = onsite_score(at)

print("Full scores: " + str( [f"{k}:{v:.3f}" for k, v in fs.items()] ) )
print("Full scores: " + str( [f"{k}:{v:.3f}" for k, v in gs.items()] ) )
print("Full scores: " + str( [f"{k}:{v:.3f}" for k, v in scores.items()] ) )
