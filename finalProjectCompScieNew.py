import Draw
import random

#"I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academicintegrity policy of the CS department.”



# authorized global variable: 
qBank=[	
	
# Science Category or qbank[0] 
[["Science", "What part of the atom has no electric charge?", "Proton","*Neutron", "electron","Neucleous"],
["Science", "Meteorology is the study of...?", "Meteors", "Outer Space","*The Weather","The moon"],
["Science", "What is the largest known mammel?","*Antarctic blue whale", " elephants", "hippos", "Killer whale"], 
["Science"," How many elements are there in the periodic \ntable?","150","200","*118","88"],
["Science","How many bones do sharks have in total?", "Three","Ten","*Zero", "Twenty"], 
["Science", "Which part of the brain deals\n with hearning and language?", "The frontal lobe", "*The temporal Lobe", "Occipital Lobe", "Brain Stem"],
["Science","What does ATP stand for?", "*Adenine Triphosphate","Add Together Potential (Energy)", "Amino Acids Triphosphates", "Adenine Triphosphates"],
["Science", "How long is the combined length of\n the small and large intestines?", "5 feet or more", "8 feet or more", "10 feet or more", "*15 feet or more"], 
["Science", "Hurricanes only form over...", "Deserts", "lakes", "*warm oceans","cold oceans"],
["Science", "What did Albert Einstein win the Nobel Prize\n for in 1921?","Relativity", "Photoelectric Effect","*Zero-point energy","Wave-particle duality"],
["Science", "Who is considered the founder of the modern\n science of genetics?","*Gregor mendel", "Dmitiri Mendeleev", "Ernest Rutherford", "Francis Crick"],
["Science", "What hormone does the pancreas produce?","Adrenaline","Estrogen","Testosterone","*Insulin"],
["Science","What is the function of kidneys\n in the human body?", "Maintain Acid-Base Balance", "Remove Waste", "Regulate blood pressure","*All of the above"], 
["Science", "What is the chemical symbol for\n silver?", "Si","Au","*Ag","Pb"],
["Science","How many legs do spiders have?","*8","12","6","2"],
["Science", "What is the thinnest layer of the Earth?","Mantle","Outer Core","Inner core","*Crust"],
["Science","Which of the following is not \nconsidered a greenhouse gas?","carbon dioxide","ozone","water vapor","*oxegyn"],
["Science","What is Avagodro's number?", "3.1415","*6.02*10^23","3*10^8","5"],
["Science", "Who created the equation e=mc^2?", " Hannah Montana"," Ariel Melnitsky","*Albert Einstien","Newton"],
["Science","What does DNA stand for?","*Deoxyribonucleic acid","deonano-Adenine","Deoxyribo-Acid","Doner-acid"],
["Science","Which isn't a protien?","Enzymes","antibodies","Helicases","*peristalsis"],
["Science","Who was the first women Noble-Prize winner?", "Liesa Meitner","*Marie Curie","Jane Auston","Rosa Parks"],
["Science","How many pieces\n of toast could a single bolt of lightning cook?","1000","10000","50000","*100000"],
["Science","What is the smallest unit of living things?","atoms","protons","*Cells","Nucleuses"], 
["Science", "What bond involves mutual\n sharing of electrons?","*Covalent","Ionic", "Multi-nucleotide-bonds","Chemical-recombination"], 
["Science", "How many bones are there in the human body?", "106","400","250","*206"],
["Science","The concept of gravity was discovered\n by which famous physicist?","Rutherford","Thompson","*Isaac Newton","Albert Einstein"],
["Science", "What is the most abundant\ngas in the atmosphere?", "*Nitrogen","Oxegyn","Carbon Dioxide","Neon"], 
["Science","Roughly how long does it take\n for sun light to reach the Earth?","8 hours","8years","*8 minutes", "8 seconds"], 
["Science","What is the name of the first satellite\n to orbit the earth?","*Grover","*Sputnik","Spacecraft-29","Rover"],
["Science","What is the study of mushrooms called?","*Fungal Biology","Mushrology","fungoo","yeastology"], 
["Science","What is the only letter not\n in the periodic table?", "A","Z","X","*Q"],
["Science","What is the only even Prime Number","100","52","4","*2"], 
["Science","In what year was Pluto deemed\n a dwarf planet?","1901","*2006","2010","1995"]


],
#History Category or qBank[1]
[
	["History","What is another name for the movement\n Martin Luther began which is also known as a\n religion crisis in the Catholic Church?","Renaissance","*Reformation","Age of Chivalry","The religous revolution"], 
["History","Who conquered the Aztec empire?","*Hernando Cortez","Francisco Pizarro","Redinand Magellan","Vasco Nunez de Balboa"], 
["History","What German telegram intended to go to\n Mexico was intercepted by the British?","The Final telegram", "The Communist party telegram","The Nazi Party telegram","*The Zimmerman Telegram"],
["History","What type of plane dropped the first atomic bomb?","An American A-28 bomber", "*An American B-29 bomber.","A Russian B-29 bomber","A chinease B-29 bomber"],
["History", "What was the name of the research and development\n project that developed the first\n atomic bomb?","The Atomic project","The final project","*The Manhatten Project","The Hiroshema Nagasaki project"],
["History","Which historical figure lived \nbetween the years of \n1815 and 1898?","*Otto von Bismarck","Thomas Jefferson","Grigori Rasputin","Mohandas K. Gandhi"],
["History","Who was the first Western explorer to reach China?","Ferdinand Magellan","James Cook","Sir Francis Drake","*Marco Polo"],
["History","Prime Minister Golda Meir was the\n leader in what country?","Pakistan","India","*Israel","Peru"],
["History","The Hundred Years War was fought\n between which two countries?","*France and England","Italy and Greece","England and Germany","Spain and Italy"],
["History","Where did the Industrial Revolution begin?","United States","France","Germany","*England"],
["History","The United States bought Alazka\n from which country?","Argentina","France","*Russia","Italy"],
["History","What was the name of the series of programs\n and projects President Franklin D. Roosevelt enacted\n during the Great Depression?","The Best Deal","*The New Deal","The Economic Resolution","Don't be depressed anymore"],
["History","The Shot Heard Around The World\n describes the beginnign of which battles\n in the American Revolution?","The Battle of Fort Sumter","*The Battle of Lexington and Concord","The Battle of Gettysburg","The Battle of Antietam" ],
["History","What country did the U.S. men’s\n Olympic hockey team defeat in the semi-finals\n of the 1980 Winter Olympics commonly known as the “Miracle on Ice”?","Italy","France","China","*The Soviet Union"],
["History","What Monarch sent Christopher Columbus\n to explore the New World?","Queen Elizabeth","Fredrick II","*King Ferdinand","Queen Victoria"],
["History","What year did the French Revolution start?","1650","*1789","1800","historians are unsure"],
["History","Who is commonly referred to as\n the person who created \nthe first printing press?","Newton","Thomas Edison","*Johannes Gutenberg","John Green"],
["History","Which of the following names is\n the name of a ruler of the Mongol Empire?","Cleopatra","Chernobyl","Leader Joi","*Genghis Khan"],
["History","What was the name of\n the nuclear power plant that was the\n site of a nuclear disaster in April 1986?","*Chernobyl","Antigua","Uzbekistan","Mesopotamia"],
["History","During World War II,\n the Allied troops stormed the beaches of Normandy.\n Which country is Normandy in?","Greece","*France","Italy","Japan"],
["History","Mount Vesuvius erupted in 79AD\nand devastated which two Roman cities?","*Pompeii","Constantinople","Carthage","Ephesus"],
["History", "Which two city-states fought in the\nPeloponnesian War?","Thebes and Argos","Rodos and Argos","Cornith and syracuse","*Athens and\n Sparta"],
["History","When were the Middle Ages?","4th Century CE","3rd Centruy CE","*5th Century CE","1995"],
["History","Which was not a member\n of the allied forces during World War II?","The US","England","Russia","*Japan"],
["History","When was the Eiffel Tower completed?","February 3,2003","March 4 1999","April 1,1900","*March 31,1889"],
["History","In which battle were\n the first shots of the civil war shot?","*Fort Sumpter","Gettysberg","Fort Sumpter","The Boston Tea Party"],
["History","Which land didn't Israel gain control\n over in the 6-day war?","Golan Heights","Sainai Peninsula","West Bank","*Eqypt"],
["History","Maimonadies was born in..","*Cordoba Spain","Egypt","london","Morocco"], 
["History","What city was the first capital of the United States?","Washington-DC","Maryland","*Philidelphia","Miami"],
["History","When did women gain the right to vote?","1820","2020","*1920","1940"], 
["History", "Who painted the ceiling\n of the Sistine Chapel?" ,"Robert Oppenheimer","*Michelangelo","Leonardo Di Vinci","Pablo Picasso"], 
["History","In what year did India gain\n independence from Britain?", "*1947","1980","1845","2000"],
["History","Who was the leader of Norh Vietnam\n during the Vietnam War?","Vo Nguyen Giap","Pham Tuam","Tran Hung Dao","*Ho Chi Minh"], 
["History","Who was Lenin's successor?", "Karl Marx","Mao Zedong","Kim II-sung","*Joseph Stalin"], 
["History","Who was the president of the\n United States during WWI?","Lincon","Woodrow Wilson","Obama","Warren G.Harding"]

],
#Geography or qBank[2]
[
	["Geography","How many continents are there?","*7","6","4","2"],
["Geography","What is the largest continent by land area?","Antartica","*Asia","Africa","Europe"],
["Geography","How many oceans are there","*5","3","7","9"],
["Geography","Which country has the largest population in the\n world?","India","Great Britan","United States","*China"],
["Geography","Which ocean lies between Australia and Africa?","Pacific","Southern","*Indian","Atlantic"],
["Geography","Which is the longest river in the world?","Yangzi","Mississippi","Mekong","*Nile"],
["Geography","Which mountain range lies between China and India?","Andes","Zangros Mountans","*Himalayas","Ural Mountains"],
["Geography","What is the longest river in Europe?","*Volga","Dnieper","Rhine","Danube"],
["Geography","Which of these cities is NOT in Europe?","Paris","*Armenia","Rome","Romania"],
["Geography","Which continent has the most countries?","Asia","Europe","*Africa","South America"],
["Geography","Which of these states in the US has the most\n coastline?","*Florida","California","Texas","Maine"],
["Geography","Beginning in the Swiss Alps,\n where does the Rhine River end?","*Netherlands","France","Germany","Italy"],
["Geography","Which of these countries is NOT on the equator?","Brazil","*Papua New Guinea","Ecuador","Uganda"],
["Geography","What is the largest US state by land area?","*Alaska","Texas","Montana","California"],
["Geography","Where are the Ural Mountains located?","Eastern Russia","Eastern China","Japan","*Western Russia"], 
["Geography","What is the capital of Jamaica?","Jamaica city","Mecca","*Kingston","Portmore"],
["Geography","What is the only country\n that borders the United Kingdom?","Scotland","*Ireland","Portugal","Morrocco"], 
["Geography", "What is the coldest sea on earth?","*Artic","Pacific","Atlantic","Mediteranean"], 
["Geography","How many countries are there in Africa?","24","34","44","*54"], 
["Geography","Which country has the most volcanos?", "Guatimala","*Indonesia","Hawaii","France"],
["Geography","Which state was\n created over millions of years as\n the result of a hot spot in the\n Pacific Ocean?","*Hawaii","Oregon","Washington","Florida"]





], 
# Movies or qbank[3]
[
	["Movies"," What was Aladdin doing\n when we first see him in the movie?","Jumping from a roof-top","Eating a piece of bread","*Stealing a piece of bread","Talking to his monkey"],
 ["Movies","Who directed the\n movie Schindler's List?","Albert Einstien","Micheal Mann","*Steven Spielberg","Irwin Winkler"],
 ["Movies","Which Disney movie was the first\n full-length animated feature produced in\n the United States?","*Snow White and the Seven Dwarfs","Sleeping Beauty","Cinderella","Marry Poppins"],
 ["Movies","In the Disney Film,\n The Little Mermaid, what does Ariel call\n the fork in her collection of human objects?", "Thing-a-mabob","spoon","Knife","*Dinglehopper"],
 ["Movies","What is the name\n of Repunsal's chameleon in Disney's movie Tangled?","Cherio","*Pascal","Henry","Perry"],
 ["Movies","In the film Titanic, where was\n Jack Dawson from?","Florida","*Wisconsin","Kansas","Texas"],
 ["Movies","In the Matrix,\n on what level do Neo and Trinity stop the elevator\n after the lobby shootout?","*41","61","51","31"],
 ["Movies","In Kung Fu Panda,\n Mr.Ping is a what?","*Goose","Panda","Monkey","Fox"],
 ["Movies","How many fingers do \nthey hold up as salute in the Hunger Games Trilogy?","Two","Four","Five","*Three"],
 ["Movies","What was the last name \nof Edward and his family in the Twilight series?","*Cullen","Smith","Jones","Sharon"],
 ["Movies","How many staircases\n does Hogwarts have in Harry Potter?","100","*142","152","162"],
 ["Movies","What is Harry's wand's core?","*Pheonix feather","Dragon's horn","Unicorn feather","Tear of a monster"],
 ["Movies","What are the names\n of the stepsisters from Disney's Cinderella?","Sarah and Jasmine","*Anastasia and Drizella","Rachel and Leah", "Bilha and Zilpah"],
 ["Movies","What name does Ursula use\n when she disguises herself to impersonate Ariel?","Sarah","Elizabeth","*Vanessa","Abigail"],
 ["Movies","Where were The Lord of the Rings movies filmed","Ireland","Iceland","Austrailia","*New Zealand"],
 ["Movies","Which is not the name of a child selected\n to tour the Wonka factory in Willy Wonka\n and the Chocolate Factory?", "Veruca Salt","Mike Teave","Charlie Bucket","*Billy Warp"],
 ["Movies","What is name of the fictional\n land where Frozen takes place?","Florin","*Arendalle","Florinn","Grimm"],
 ["Movies","In the Matrix,\n what color are the two pills that\n Morpheus chooses between?","Yellow and orange","*Red and Blue","Green and Red","Purple and pink" ],
 ["Movies", "Which is not one of the\n seven dwarfs?","Bashful","*Angry","Dopey","Doc"],
 ["Movies", "In Bambi,\n what is the name of Bambi's skunk friend?","*Flower","Julie","Rochel","Rose" ],
 ["Movies", "In Forrest Gump, according to Forrest's mom\n what is life like?","a closet","*a box of chocolates","Comp 1320","a telephone"],
 ["Movies", "In the hunger games, Katniss volunteers for...","Her Mother","Her boyfriend","*Her sister","Her bestfriend"],
 ["Movies", "What does Gru plan on stealing in Despicable Me?","*The Moon","The pink panther diamond","The US constitution","10000 dollars"],
 ["Movies","Whats the name of Hazel's favorite author\n in the Fault in Our Stars?","Shakespear","Emerson","Jane Auston","*Peter Van Houton"],
 ["Movies", "In Princess Diaries, Genovia is famous for...","Apples","Oranges","*Pears","Watermelons"],
 ["Movies", "What does John Keating teach\n in Dead Poets Society?","Math","*English","Science", "Comp 1320"],
 ["Movies", "Where does Night at the Museum take place?","The met","The Louvre","The Istrael Museum","*The Museum of Natural History"],
 ["Movies", "In Home Alone, Kevin's family travels to ____ \n leaving Kevin Home Alone.","*Paris","Italy","Israel","Stern College For Women"]
 
 
 ]
]


# Creates the squares on the screen that each correspond to a different category 
# (Spinner uses this function to display the spinner graphic)
# Parameters color x y name x2 y2 and font are passed into this function 
# So that each time it is called, the square on the category's 
# corresponding quarter of the screen is displayed. 

def displaySquares(color, x, y, name,x2,y2,font, time): 
	Draw.clear()
	Draw.setFontSize(font)
	# set the color to the color of the category (from the parameter). 
	Draw.setColor(color)
	# Create a rectangle at parameters x and y 
	Draw.filledRect(x,y,250,250)
	Draw.setColor(Draw.BLACK)
	Draw.rect(x,y,250,250)
	# Create another white rectangle in the middle at x+20 so that 
	# it appears in the middle of the outer colored rectangle and 
	# make it smaller than the outer rectangle
	Draw.setColor(Draw.WHITE) 
	Draw.filledRect(x+20,y+20,200,200)
	# Display the category inside the middle of the box
	Draw.setColor(Draw.BLACK)
	Draw.setFontFamily('Chalkboard') 
	Draw.string(name,x2,y2)
	# Show the box, depending on if the box was chosen or not, time will
	# be smaller or larger.
	Draw.show(time)
	

# Choose a random Category

def getCategory():# no inputs returns the randomly chosen category
	
	# if the int is zero, for example, that means that the zeroth element 
	# of qBank was chosen: The chosen category in this example would be 
	# Science. 
	
	chosenCategory= random.randint(0,3)
	
	return chosenCategory

# Display the spinner on the screen 

def spinner(chosenCategory):# input the chosen random category and also return it.
	
	
	boxes=['science','History','geography','movies']
	for x in range(4):
		# loop through displaying the different boxes five times
		# This will give the illusion of a 'spinner'. 
		for i in range(len(boxes)):
			if i==0:
				displaySquares(Draw.RED, 0,25,'Science',40,100,50,150)
			elif i==1: 
				displaySquares(Draw.YELLOW,250,25,'History',300,100,50,150)
			elif i==2: 
				displaySquares(Draw.ORANGE,250,275,'Geography',273,350,38,150)
			elif i==3: 
				displaySquares(Draw.GREEN,0,265,'Movies',30,350,50,150)
				
				
	for c in range(len(boxes)):
		# loop through the categories above in boxes. 
		# if the chosen category is zero, display Zero, but for much
		# longer to indicate that zero was chosen.(for example)
		if c==0 and c==chosenCategory: 
			displaySquares(Draw.RED, 0,25,'Science',40,100,50,400)
			

			
		elif c==1 and c==chosenCategory: 
			displaySquares(Draw.YELLOW,250,25,'History',300,100,50,400)
			

			
		elif c==2 and c==chosenCategory:
			displaySquares(Draw.ORANGE,250,275,'Geography',273,350,38,400)
			
			
		elif c==3 and c==chosenCategory: 
			displaySquares(Draw.GREEN,0,265,'Movies',30,350,50,400)
			
	Draw.show(100)
	Draw.clear()
	
	return chosenCategory

#choose a question from the chosen category

def chooseQuestion(chosenCategory,numZero,numOne,numTwo,numThree): # input the category
	# input the number of times that each category was chosen so that the user
	# doesn't get the same question each time. 
	
	
	theQ=[]
	
	if chosenCategory==0: 
		theQ=qBank[0][numZero] # if the chosen category is science
		numZero+=1 # display the first question then increment 
		# numZero so that next time, the second question shows. 
	elif chosenCategory==1: # The same goes for each category. 
		theQ=qBank[1][numOne]
		numOne+=1
	elif chosenCategory==2: 
		theQ=qBank[2][numTwo]
		numTwo+=1
	elif chosenCategory==3: 
		theQ=qBank[3][numThree]
		numThree+=1
	
	# return the chosen question and the updated number of times that 
	# the category was chosen so that the game will give the next question.
	return theQ,numZero,numOne,numTwo,numThree

# Display the question and answers in the correct boxes. 
# Make sure to display the correct answer without a star. 
# Save the xy coordinates of the correct answer. 

def display(theQuestion): # Input the question and return the correct answer's xy coordinates.
	
	# Create the empty boxes where the question, category, and answer 
	# choices will be displayed
	Draw.setColor(Draw.BLACK)
	catDisp=Draw.rect(110,10,275,55)
	Qdisp=Draw.rect(50,100,400,100)
	aDisp=Draw.rect(110,250,275,50)
	bDisp=Draw.rect(110,300,275,50)
	cDisp=Draw.rect(110,350,275,50)
	dDisp=Draw.rect(110,400,275,50)
	
	# This variable will save the correct answer's x-y coordinates. 
	correctAnswerXY=[]
	

	# This loop displays each element of the question in its correct box 
	
	for i in range(6): 
		# if i is 0 then put the zeroth element of the question in the 
		# first box. 
		if i==0: 
			Draw.setFontSize(30)
			Draw.setFontFamily('Chalkboard') 
			Draw.string(theQuestion[0],190,20)
		# if i is 1 then put the first element of the question into the 
		# second box. 
		elif i==1: 
			Draw.setFontSize(15)
			Draw.string(theQuestion[1],70,120)
		# if i is greator than or equal to two then the program is 
		# up to putting the answers in the correct boxes. 
		elif i>=2: 
			# if the first element of the question is a star, 
			# then it is the correct answer. 
			
			# so, in that case display the answer choice without 
			# the star. 
			
			# save the correct answer's xy coordinates. 
			
			if theQuestion[i][0]=='*' and i==2: # if it has a star	    
					theQuestion[2]=theQuestion[2][1:]
					Draw.string(theQuestion[2],130,260) 
					correctAnswerXY+=[110,250,275,55]
			# if the answer choice isn't the correct answer 
			#( it doesn't start with a star) then display it 
			# without a star. 
			
			elif theQuestion[i][0]!='*' and i==2: 
				Draw.string(theQuestion[2],130,260)
					
			elif theQuestion[i][0]=='*' and i==3:	    
				theQuestion[3]=theQuestion[3][1:]
				Draw.string(theQuestion[3],130,320) 
				correctAnswerXY+=[110,300,275,55]
				
			elif theQuestion[i][0]!='*' and i==3: 
				Draw.string(theQuestion[3],130,320) 
			
			elif theQuestion[i][0]=='*' and i==4: 
				theQuestion[4]=theQuestion[4][1:]
				Draw.string(theQuestion[4],130,375)
				correctAnswerXY+=[110,350,275,55]
			elif theQuestion[i][0]!='*' and i==4: 
				Draw.string(theQuestion[4],130,375)
				
			elif theQuestion[i][0]=='*' and i==5: 
				theQuestion[5]=theQuestion[5][1:]
				Draw.string(theQuestion[5],130,425) 
				correctAnswerXY+=[110,400,275,55]
				
			elif theQuestion[i][0] !='*' and i==5: 
				Draw.string(theQuestion[5],130,425) 
	
	Draw.show()
	
	return correctAnswerXY



def getClick(correctAnswerXY): # input the correct answer's xy coordinates 
	# return if they answered wrong or right.  
	
	wrongCount=0
	pressed=0
	

	while pressed<1: # so that you only press one answer
		if Draw.mousePressed(): # if you press, save the x-y of the cursor
			x=Draw.mouseX()
			y=Draw.mouseY() 
			if x>=110 and x<=110+275 and y>=250 and y<=450: # make 
				# sure the user pressed in a box. 
				# if the user presses anywhere on the screen, 
				# then nothing should happen 
				pressed+=1
				# if the user pressed one of the answer choices, 
				# then the user doesn't get another try: 
				# fall out of the while loop. 
				
				if (x>=110 and x<=110+275) and y>=correctAnswerXY[1] and y<=correctAnswerXY[1]+55:
					# if the user's click falls in the correct 
					# answer's x-y box
					correct() # display correct on the screen. 
					
					
				else:
					wrongCount+=1# if the user's click falls in 
					# an incorrect box. incriment wrongCount. 
					# and then display incorrect on the 
					# screen. 
					incorrect()
			
				
			
	
	return wrongCount 

def correct(): # display correct on the screen 
	Draw.clear()
	Draw.setFontSize(60)
	Draw.string("Correct!",150,200) 
	Draw.show(1000)
	
def incorrect(): #display incorrect on the screen 
	
	Draw.clear()
	Draw.setFontSize(60)
	Draw.string("Incorrect",150,200) 
	Draw.show(1000)
	
def shuffle(): # this will be called at the begining of the game so that each 
	       # time the user plays the questions will be shuffled
	random.shuffle(qBank[0]) 
	random.shuffle(qBank[1]) 
	random.shuffle(qBank[2]) 
	random.shuffle(qBank[3])
	
def flushClicks(): # Ensures that when you click while the spinner is spinning 
# The program is not taking input. 
	while Draw.mousePressed():
		Draw.mouseX()
		Draw.mouseY()

def main():
	# at the start of the game the score and times each category has been run is zero. 
	score=0 
	numZero=0
	numOne=0
	numTwo=0
	numThree=0
	wrongCount=0
	
	# Shuffle the questions in random order 
	shuffle()
	
	while wrongCount<=2: # while the user didn't get three wrong. (0,1,2)
		theCat=getCategory() # get a random category 
		spinner(theCat)# spin the spinner 
		theQ,numZero,numOne,numTwo,numThree=chooseQuestion(theCat,numZero,numOne,numTwo,numThree) 
		# get the question and and the number of times each category was chosen
		correct=display(theQ) # display the question and get the correct xy coordinates 
		
		flushClicks() # make sure not to continue getting input from the user while
		# the spinner spins 
		
		# increment wrong count if the user got one wrong. 
		wrongCount+=getClick(correct)
		
		# if there were three wrong, fall out of the while loop. 
	# It was game over
	
	Draw.clear() 	
	Draw.setFontSize(50)
	# display the score. The score is the total number of questions answered
	# but subtract 3 because the user got three wrong. 
	Draw.string("Your Score: "+ str(numZero+numOne+numTwo+numThree-3),100,100) 
	Draw.show()	
			
main()
