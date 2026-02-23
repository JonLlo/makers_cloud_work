require_relative '../lib/apprentice.rb'
require_relative '../lib/challenge.rb'

RSpec.describe Apprentice do

  subject do
    Apprentice.new(
      'Joe',
      'Mangel',
      'Software Development',
      'BitArt Ltd'
    )
  end

  let(:mastery_quizzes) { Challenge.new('Mastery Quizzes') }

  describe '#first_name' do
    it "returns the apprentice's first name" do
      expect(subject.first_name).to eq 'Joe'
    end
  end

  describe '#last_name' do
    it "returns the apprentice's last name" do
      expect(subject.last_name).to eq 'Mangel'
    end
  end

  describe '#full_name' do
    it "returns the apprentice's full name" do
      expect(subject.full_name).to eq 'Joe Mangel'
    end
  end

  describe '#program' do
    it "returns the apprenitice's program" do
      expect(subject.program).to eq 'Software Development'
    end
  end

  describe '#employer' do
    it "returns the apprentice's employer" do
      expect(subject.employer).to eq 'BitArt Ltd'
    end
  end

  describe '#summary' do
    it 'summarises all info about the apprentice' do
      expect(subject.summary).to eq(
        "Joe Mangel, Software Development Apprentice, January 2050 - BitArt Ltd"
      )
    end
  end

  describe '#assign' do
    it 'adds a challenge to challenges' do
      expect { subject.assign(mastery_quizzes) }
        .to change {subject.challenges.count}
        .by 1
    end
  end

  describe '#challenges' do
    it 'returns an array of assigned challenges, with the state of each one' do
      subject.assign(mastery_quizzes)
      expect(subject.challenges).to eq(
        ['Mastery Quizzes - incomplete']
      )
    end
  end

  describe '#complete_challenge' do
    it 'takes the name of a challenge as an arg and marks is as complete' do
      subject.assign(mastery_quizzes)
      subject.complete_challenge('Mastery Quizzes')
      expect(subject.challenges).to eq(
        ['Mastery Quizzes - complete']
      )
    end
  end
end
