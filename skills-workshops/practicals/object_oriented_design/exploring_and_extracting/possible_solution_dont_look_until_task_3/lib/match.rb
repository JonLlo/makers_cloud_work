class Match
  attr_reader :id, :winner

  def initialize(id, player_1, player_2)
    @id = id
    @player_1 = player_1
    @player_2 = player_2
    @winner = nil
  end

  def show
    string = "Match #{@id}: #{@player_1} vs #{@player_2}"
    if @winner != nil
      string += ", #{@winner} wins"
    end
    string
  end

  def record_winner(winner)
    raise "Wrong player name: #{winner}." if ![@player_1, @player_2].include?(winner)
    @winner = winner
  end
end