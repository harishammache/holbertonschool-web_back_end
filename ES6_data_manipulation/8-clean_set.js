function cleanSet(set, startString) {
  const resultArray = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));
  return resultArray.join('-');
}

export default cleanSet;
