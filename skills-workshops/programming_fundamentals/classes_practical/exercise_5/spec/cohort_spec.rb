require_relative '../lib/cohort.rb'

RSpec.describe Cohort do

  subject { Cohort.new('January 2050') }
  let(:mathilde) {Apprentice.new('Mathilde', 'Legrand', 'Dev Ops', 'Macrosoft')   }
  let(:claude)   {Apprentice.new('Claude', 'Petit', 'Software Development', 'Hooli')}

  describe '#name' do
    it 'returns the name of the cohort' do
      expect(subject.name).to eq 'January 2050'
    end
  end

  describe '#add' do
    it 'adds an apprentice to the cohort' do
      subject.add(mathilde)
      subject.add(claude)
      expect(subject.apprentices).to eq [
        mathilde,
        claude
      ]
    end
  end

  describe '#remove' do
    it 'remove an apprentice from the cohort' do
      subject.add(mathilde)
      subject.add(claude)
      subject.remove('Mathilde Legrand')
      expect(subject.apprentices).to eq [claude]
    end
  end

  describe '#dev_ops_apprentices' do
    it 'returns only the dev ops apprentices' do
      expect(subject.dev_ops_apprentices).to eq [mathilde]
    end
  end

  describe '#software_development_apprentices' do
    it 'returns only the software development apprentices' do
      expect(subject.software_development_apprentices).to eq [claude]
    end
  end

  describe '#assign' do
    it 'assigns a challenge to every member of the cohort' do
      subject.assign('Mastery Quizzes')
      expect(cohort.apprentices.map(&:challenges)).to eq(
        [
          ['Mastery Quizzes - incomplete'],
          ['Mastery Quizzes - incomplete']
        ]
      )
    end
  end
end
