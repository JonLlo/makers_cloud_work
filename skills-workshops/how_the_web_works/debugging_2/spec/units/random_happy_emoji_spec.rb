# coding: utf-8

require 'random_happy_emoji'

describe RandomHappyEmoji do
  describe '::new' do
    it 'returns a :D emoji as a string', focus: true do
      allow_any_instance_of(RandomHappyEmoji).to receive(:random_index).and_return(0)

      expect(RandomHappyEmoji.new.get_emoji).to eq ":D"
    end

    it 'returns a :) emoji as a string', focus: true do
      allow_any_instance_of(RandomHappyEmoji).to receive(:random_index).and_return(1)

      expect(RandomHappyEmoji.new.get_emoji).to eq ":)"
    end
  end
end
