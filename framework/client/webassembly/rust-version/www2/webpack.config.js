const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');
const WasmPackPlugin = require("@wasm-tool/wasm-pack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const { config } = require('process');

module.exports = {
    entry: './index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'index.js',
    },
    plugins: [
        new CopyWebpackPlugin([
            {
              from: path.resolve(__dirname, './index.html'),
              to: path.resolve(__dirname, './dist/index.html'),
              flatten: true
            }
          ])
    ],
    mode: 'development'
};