require_relative '../lib/apprentice.rb'

RSpec.describe Apprentice do

  subject do
    Apprentice.new(
      'Joe',
      'Mangel',
      'Software Development',
      'BitArt Ltd'
    )
  end

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
        "Joe Mangel, Software Development Apprentice - BitArt Ltd"
      )
    end
  end
end
