//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const toRna = (dna_strand) => {
  let dna_to_rna_dict = {"G":"C", "C":"G","T":"A","A":"U"};
  return dna_strand==''?'': Array.from(dna_strand).map(dna => dna_to_rna_dict[dna]).join('');
};
