require 'appointment'

describe Appointment do
  subject(:appointment) { described_class.new(time, end_time, "Test appointment", "50 Commercial Street London") }
  let(:time) { Time.now }
  let(:end_time) { Time.now + 3600 }

  describe '#title' do
    it 'has a title' do
      expect(appointment.title).to eq "Test appointment"
    end
  end

  it { is_expected.to respond_to :start_time }
  it { is_expected.to respond_to :end_time }

  describe '#pretty_location' do
    it 'pretty-prints the location' do
      expect(appointment.pretty_location).to include "E1 6LT"
    end
  end
end
