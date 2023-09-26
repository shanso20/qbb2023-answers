Exercise 1:
Step 1.1) 	How many 100bp reads are needed to sequence a 1Mbp genome to 3x coverage?
				1Mbp x 3 / 100bp = 0.03M = 3 x 10^4 = 30,000 reads

Step 1.3) 	In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
				In this simulation, there are 52127 bases with 0 coverage (5.2127% of the genome)

Step 1.4) 	In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
				In this simulation, there are 122 bases with 0 coverage (0.0122% of the genome)
			How well does this match Poisson expectations? How well does the normal distribution fit the data?
				The Poisson curve predicts there will be close to 0 bases with no coverage (specifically, it predicts 45bp to have 0 coverage). On the scale of 1Mbp, 122 is quite close to this expectation, so I'd say this matches Poisson expectations pretty well. The normal distribution seems to fit the data well, though the curve is slightly higher than the simulation on the low-coverage end, and lower on the high-coverage end.

Step 1.5)	In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
				In this simulation, there are 9 bases with 0 coverage (0.0009% of the genome)
			How well does this match Poisson expectations? How well does the normal distribution fit the data?
				The Poisson curve again predicts there will be close to 0 bases with no coverage (but this time even closer--9.358e-8, which is essentially 0). On the scale of 1Mbp, 9 is very close to 0, so this matches Poisson expectations very well. The normal distributino fits the data even closer than in the simulation with mean coverage = 10x, though I can still see that the curve very slightly over-estimates probabilities at low coverage (and the inverse at high coverage).


Exercise 2:-------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 2.4)	Record the command you used in your READMD.md
				dot -Tpng -oex2_digraph.png test.dot

Step 2.5)	Assume that the maximum number of occurrences of any 3-mer in the actual genome is 5. Using your graph from Step 2.4, write one possible genome sequence 				that would produce these reads. Record your answer in your README.md
				ATTGATTCTTATTCATTT

Step 2.6)	In a few sentences, what would it take to accurately reconstruct the sequence of the genome? Record your answer in your README.md
				In order to accurately reconstruct the genome sequence, I would need a set of longer reads in addition to the reads/ deBruijn graph that I already have. With the current deBruijn graph, I could theoretically continue a sequence forever, but a set of longer reads would inform me of paths/ repeats not to take and provide guidance of when to stop repeating in loops and end the sequence. In essence, a set of longer reads could help simplify the de Bruijin graph until there is a straight path from start to finish with no loops to get stuck in.

Exercise 3:------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 3.1) 	Use ChatGPT (or Bard or your favorite LLM) to write an essay on why you are interested in genomics. Make sure to ask for references. Record both your prompt
			(s) and the output from the LLMin your README.md.
				My promt to ChatGPT: write me an essay about why I am interested in genomics and provide references
				Essay: Title: Unveiling the Code of Life: My Passion for Genomics

Introduction

Genomics, the study of an organism's complete set of genes and their functions, has emerged as a transformative field with profound implications for our understanding of life, healthcare, and the environment. My profound interest in genomics is driven by its potential to unravel the mysteries of genetics, shape personalized medicine, address global challenges, and inspire ethical discussions. This essay explores the multifaceted reasons behind my fascination with genomics while drawing upon reputable references to support my perspective.

Genomics as the Blueprint of Life
Genomics serves as the blueprint of life, offering an unparalleled view into the genetic information that governs all living organisms. The ability to decode genomes has deepened our comprehension of biological processes and evolution. As I delve into this field, I am captivated by the intricate genetic codes that determine the characteristics and functions of organisms, from the humble bacterium to the complexities of the human genome (Alberts et al., 2014).

Personalized Medicine and Precision Healthcare
Genomics has ushered in the era of personalized medicine, where treatment plans are tailored to individual genetic profiles. The promise of more effective, precise, and personalized healthcare is a compelling reason for my interest in genomics (Collins & Varmus, 2015). The knowledge that genomics can guide early disease detection and therapy selection, minimizing side effects and maximizing therapeutic efficacy, fuels my passion to contribute to this transformative aspect of healthcare.

Agricultural Advancements and Food Security
Genomics extends its influence to agriculture, offering solutions to address the challenges of feeding a growing global population. By studying the genomes of crops and livestock, scientists can develop hardier, more productive strains and sustainable agricultural practices (Varshney et al., 2020). I am intrigued by the prospect of using genomics to mitigate food scarcity and enhance food security.

Ethical Considerations and Societal Impact
The ethical dimensions of genomics are both captivating and challenging. The responsible use of genetic information, privacy concerns, and potential discrimination raise profound ethical questions (Knoppers et al., 2019). Engaging in ethical discourse and helping shape guidelines for the ethical practice of genomics excites me. This aspect of the field emphasizes the importance of considering the societal and ethical impact of scientific advancements.

Continual Advancements and Discovery
Genomics is marked by rapid technological advancements and a constant stream of discoveries. Cutting-edge technologies like CRISPR gene editing and high-throughput sequencing continue to redefine the boundaries of genomics research (Jinek et al., 2012; Metzker, 2010). The dynamic nature of the field ensures that there will always be new avenues to explore and contribute to.

Conclusion

My interest in genomics stems from its role as the code of life, its potential to revolutionize healthcare and agriculture, its ethical complexities, and its ever-evolving nature. Genomics represents a powerful tool to understand, improve, and ethically navigate the biological world. As I pursue my passion for genomics, I am committed to contributing to this transformative field and addressing its ethical implications, all while remaining inspired by its continuous advancements and discoveries.

References:

Alberts, B., Johnson, A., Lewis, J., Raff, M., Roberts, K., & Walter, P. (2014). Molecular Biology of the Cell (6th ed.). Garland Science.
Collins, F. S., & Varmus, H. (2015). A New Initiative on Precision Medicine. New England Journal of Medicine, 372(9), 793–795.
Jinek, M., Chylinski, K., Fonfara, I., Hauer, M., Doudna, J. A., & Charpentier, E. (2012). A Programmable Dual-RNA–Guided DNA Endonuclease in Adaptive Bacterial Immunity. Science, 337(6096), 816–821.
Knoppers, B. M., Thorogood, A. M., & Laberge, C. M. (2019). Ethical Considerations in Genomic Medicine: Challenges and Opportunities for Health Care Providers. Progress in Cardiovascular Diseases, 62(1), 27–31.
Metzker, M. L. (2010). Sequencing Technologies – The Next Generation. Nature Reviews Genetics, 11(1), 31–46.
Varshney, R. K., Bansal, K. C., Aggarwal, P. K., Datta, S. K., & Craufurd, P. Q. (2020). Agricultural biotechnology for crop improvement in a variable climate: Hope or hype? Trends in Plant Science, 25(11), 1055–1076.

Step 3.2) 	In your README.md, comment on the output from the LLM: Does it make logical sense? Does it include any phrases you would not have written? Do the cited 				papers exist and support the claims from the LLM?

The essay from chatGPT does make logical sense. However, it sounds nothing like my style of writing. I am much more long-winded, while chatGPT was very concise on each of its points. In that way, the essay chatGPT wrote is more like a draft of basic points that I would flesh out more in my own version. It also used some words and phrases that I would not. For example, it titled the essay "My Passion for Genomics" and harped on the word "passion" throughout much of the text, while this is a rather "cliche" sounding word (from my perspective) that I would likely never use in an essay, even if I were passionate about the subject. Beyond that, the tone of the whole essay is just a bit too... excited to have come from me (not that I think genomics is dull, I just don't write like that). In fact, in one sentence chatGPT used the wording ".... excites me". I would never use that particular phrase in my writing. I think I just tend not to be so emotional in writing in general. Also, "multifaceted", a word it used in the introduction, is a word I had entirely forgot existed and thus would be unlikely to use in writing.

As for the references: 
	The first reference (Alberts et al., 2014) is literally an entire textbook. It exists, but it is not typical to cite a whole book like that--normally, I'd expect a reference to a particular chapter. I also don't think any citation was necessary at this point, as the sentence in the essay where it was used was expressing an opinion and universal knowledge, not referencing a fact.

	The second reference (Collins et al., 2015) does exist and is a scientific article, and it also relates to healthcare in line with the point of the paragraph where it was used. However, I would personally use more direct information from the article if I were going to cite it. It doesn't seem necessary at this point.

	Jinek et al., 2012 also exists and fits well, as does Metzker (2009) and Varshney et al., 2020. 

	ChatGPT got a little sketchy with the reference to Knoppers et al. 2019. An article with a similar title exists ("Genomic medicine: challenges and opportunities for physicians"), but chatGPT changed some of the wording in the title to be more fitting to its use in the essay. It also seems to have just made up the authors entirely (at least, the authors it listed are not the authors of the article I found). I've heard of chatGPT doing this before--choosing well-known names to make references sound more credible.

	Essentially, chatGPT picked out some solid references that could be useful in a more fleshed-out paper (though not necessarily appropriate for the essay it wrote). However, it altered the title of one reference and completely fabricated the authors, showing that any references generated by chatGPT should be thoroughly checked before in an actual paper.