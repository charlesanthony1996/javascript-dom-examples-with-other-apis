const path = require("path");

module.exports = {
  entry: "./d3/example1.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js"
  }
};
