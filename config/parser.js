import * as fs from 'fs';
import * as path from 'path';

class Parser {
  constructor() {
    this.config = {
      root: path.resolve(__dirname, '..'),
      src: 'src',
      dist: 'dist',
    };
  }

  getRoot() {
    return this.config.root;
  }

  getSrc() {
    return path.join(this.config.root, this.config.src);
  }

  getDist() {
    return path.join(this.config.root, this.config.dist);
  }

  getFileContents(filePath) {
    const fileContent = fs.readFileSync(path.join(this.config.root, filePath), 'utf8');
    return fileContent;
  }

  parseFile(filePath) {
    const fileContent = this.getFileContents(filePath);
    // implement file parsing logic here
    return fileContent;
  }
}

export default Parser;