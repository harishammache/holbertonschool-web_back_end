function getListStudentIds(tableauObjets) {
  if (!Array.isArray(tableauObjets)) {
    return [];
  }

  return tableauObjets.map((etudiant) => etudiant.id);
}

export default getListStudentIds;
