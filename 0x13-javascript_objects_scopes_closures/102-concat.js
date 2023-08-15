// #!/usr/bin/node
const fs = require('fs');

async function concatFiles() {
  try {
    const content1 = await fs.promises.readFile(process.argv[2], 'utf-8');
    const content2 = await fs.promises.readFile(process.argv[3], 'utf-8');

    const concatContent = content1 + '\n' + content2;

    await fs.promises.writeFile(process.argv[4], concatContent);

    console.log(concatContent);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

concatFiles();
