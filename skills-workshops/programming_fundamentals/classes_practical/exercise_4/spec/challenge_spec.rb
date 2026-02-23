require 'challenge'

RSpec.describe Challenge do

  subject { Challenge.new("Mastery Quizzes") }

  describe '#name' do
    it 'returns the name of the challenge' do
      expect(subject.name).to eq 'Mastery Quizzes'
    end
  end

  describe '#state' do
    context 'when the challenge has not been completed' do
      it 'returns "incomplete"' do
        expect(subject.state).to eq 'incomplete'
      end
    end
  end

  describe '#complete!' do
    it 'changes state to "complete"' do
      expect { subject.complete! }
        .to change { subject.state }
        .from("incomplete")
        .to("complete")
    end
  end
end
