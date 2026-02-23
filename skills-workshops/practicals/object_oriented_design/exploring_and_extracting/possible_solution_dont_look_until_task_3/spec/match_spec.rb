require 'match'

describe Match do
  
  describe '#show' do
    it 'displays a match correctly between Alice and Bob' do
      match = Match.new(2, "Alice", "Bob")
      expect(match.show).to eq "Match 2: Alice vs Bob"
    end

    it 'displays a match correctly between Charlie and Denise' do
      match = Match.new(2, "Charlie", "Denise")
      expect(match.show).to eq "Match 2: Charlie vs Denise"
    end

    it 'displays a match with the right id' do
      match = Match.new(3, "Charlie", "Denise")
      expect(match.show).to eq "Match 3: Charlie vs Denise"
    end

    it 'displays a match with a winner' do
      match = Match.new(3, "Charlie", "Denise")
      match.record_winner("Charlie")
      expect(match.show).to eq "Match 3: Charlie vs Denise, Charlie wins"
    end
  end

  describe '#record_winner' do
    it 'gives an error if the player name is wrong' do
      match = Match.new(2, "Alice", "Bob")
      expect{match.record_winner("Charlie")}.to raise_error "Wrong player name: Charlie."
    end

    it 'records the winner correctly' do
      match = Match.new(1, "Alice", "Denise")
      match.record_winner("Alice")
      expect(match.winner).to eq "Alice"
    end

  end

end