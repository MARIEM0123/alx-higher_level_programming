#!/usr/bin/node
const dict = require('./101-data').dict;

const ttlst = Object.entries(dict);
const vls = Object.values(dict);
const vlsnq = [...new Set(vls)];
const newDict = {};
for (const j in vlsnq) {
  const list = [];
  for (const k in ttlst) {
    if (ttlst[k][1] === vlsnq[j]) {
      list.unshift(ttlst[k][0]);
    }
  }
  newDict[vlsnq[j]] = list;
}
console.log(newDict);

