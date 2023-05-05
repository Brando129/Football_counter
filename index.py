"""You are counting points for a football game, given the
amount of touchdowns, after points, and field goals find the
final points for the team and return that value."""

def final_score(touchdowns, after_points, two_point_con, field_goals):
    touchdowns = touchdowns * 6
    after_points = after_points
    two_point_con = two_point_con * 2
    field_goals = field_goals * 3
    total_points = touchdowns + after_points + two_point_con + field_goals
    return f"The teams final score is {total_points}"

print(final_score(1,1,1,1,))