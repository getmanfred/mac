import fs from "fs";
import path from "path";
import { promisify } from "util";
import { compileFromFile } from "json-schema-to-typescript";
const writeFile = promisify(fs.writeFile);
const mkdir = promisify(fs.mkdir);

const baseOutDir = "../../typescript";
const srcFilePath = path.join(__dirname, "../../schema/schema.json");
const outDir = path.join(__dirname, baseOutDir);
const outFilePath = path.join(__dirname, baseOutDir, "schema.ts");

(async () => {
  try {
    const schema = await compileFromFile(srcFilePath);
    await mkdir(outDir);
    await writeFile(outFilePath, schema);
  } catch (error) {
    console.error(error);
  }
})();
