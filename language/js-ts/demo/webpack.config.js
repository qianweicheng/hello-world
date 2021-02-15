const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');
const CopyWebpackPlugin = require("copy-webpack-plugin");
const { config } = require('process');

module.exports = {
  entry: {
    'index': __dirname + '/src/index.js',
    'test': __dirname + '/src/test.ts',
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].js',
    libraryTarget: 'window',
  },

  module: {
    rules: [
      {
        test: /\.m?js|ts$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            // It will override the babel.config.json config.
            presets: ['@babel/preset-env', "@babel/preset-typescript"]
          }
        }
      }
    ]
  },

  plugins: [
    new CopyWebpackPlugin([
        {
          from: path.resolve(__dirname, './src/index.html'),
          to: path.resolve(__dirname, './dist/index.html'),
          flatten: true
        }
      ]),
    // new HtmlWebpackPlugin(),
  ],
  mode: 'development'
};