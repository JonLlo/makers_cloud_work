describe("Pen", function() {
  let pen;
  let sheep;

  describe("#admit", function() {
    beforeEach(function() {
      pen = new Pen();
      sheep = new Sheep("bessie");
    });

    it("can admit a sheep to the pen", function() {
      pen.admit(sheep);
      expect(pen.sheepNames()).toEqual(["bessie"]);
    });
  });

  describe("#sheepNames", function() {
    let bessie, flossie;

    beforeEach(function() {
      pen = new Pen();
      bessie = new Sheep("bessie");
      flossie = new Sheep("flossie");
    });

    it("can list two sheep names", function() {
      pen.admit(bessie);
      pen.admit(flossie);
      expect(pen.sheepNames()).toEqual(["bessie", "flossie"]);
    });
  });
});
