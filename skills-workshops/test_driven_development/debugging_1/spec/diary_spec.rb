require 'diary'

describe Diary do
  subject(:diary) { described_class.new }
  let(:start_time) { Time.now }
  let(:end_time) { Time.now + 3600 }
  # times for the other appointment, which overlap with the first one
  let(:other_start_time) { start_time + 1800 }
  let(:other_end_time) { end_time + 1800 }

  let(:appointment) { appointment = double(:appointment, start_time: start_time, end_time: end_time, title: "Test appointment") }
  let(:other_appointment) { appointment = double(:appointment, start_time: other_start_time, end_time: other_end_time, title: "Test appointment") }

  describe '#make_appointment' do
    before do
      diary.add_appointment(appointment)
    end

    it 'makes an appointment' do
      expect(diary.appointments.last.title).to eq "Test appointment"
      expect(diary.appointments.last.start_time).to eq(start_time)
      expect(diary.appointments.last.end_time).to eq(end_time)
    end

    it 'raises an error if appointment times conflict' do
      expect { diary.add_appointment(other_appointment) }.to raise_error "You're not free at that time"
    end
  end
end