require_relative '../lib/cohort.rb'

RSpec.describe Cohort do

  subject { Cohort.new('January 2050') }

  describe '#name' do
    it 'returns the name of the cohort' do
      expect(subject.name).to eq 'January 2050'
    end
  end

  describe '#add' do
    it 'adds an apprentice to the cohort' do
      subject.add('Mathilde')
      subject.add('Claude')
      expect(subject.apprentices).to eq ['Mathilde', 'Claude']
    end
  end

  describe '#remove' do
    it 'remove an apprentice from the cohort' do
      subject.add('Mathilde')
      subject.add('Claude')
      subject.remove('Mathilde')
      expect(subject.apprentices).to eq ['Claude']
    end
  end
end
