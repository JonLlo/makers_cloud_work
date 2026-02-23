require 'Match'

class LeagueOrganiser

  def initialize(players)
    raise "A league needs at least two players." if players.length < 2
    @players = players
    @matches = generate_matches(@players)
  end

  def show_matches
    matches_strings = @matches.map do | match |
      match.show
    end
    puts matches_strings.join("\n")
  end

  def record_a_win(match_id, winner)
    match = @matches.find {|match| match.id == match_id}
    raise "Wrong match number: #{match_id}." if match == nil
    match.record_winner(winner)
  end

  def overall_winner
    raise "Cannot determine winner: Some matches do not have a winner yet." if @matches.any? {|match| match.winner == nil}
    return calculate_overall_winner
  end

  private

  def generate_matches(players)
    matches = players.combination(2)
    matches.map.with_index do | players, index|
      player_1, player_2 = players
      Match.new(index + 1, player_1, player_2)
    end
  end

  # buggy if more than one player has the same number of points
  def calculate_overall_winner
    points_per_player = {}
    @players.each { |name| points_per_player[name] = 0 }
    @matches.each do |match|
      points_per_player[match.winner] += 1
    end
    max_points = points_per_player.values.max
    return points_per_player.key(max_points)
  end

end