# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

# Sie können die Syntax und Semantik von Python (10)

![syntax](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/6608c57c-5253-4d7f-9015-a67b84d03120)
Der hier gezeicgte Code verwendet die Tkinter-Bibliothek, um eine grafische Benutzeroberfläche (GUI) für ein Hangman-Spiel zu erstellen.

Die erste Zeile initialisiert eine Zählervariable n auf 0. Dieser Zähler wird verwendet, um die Schaltflächen auf dem Rasterlayout der GUI zu positionieren.
Die for-Schleife iteriert über alle Großbuchstaben des ASCII-Zeichensatzes. Für jeden Buchstaben wird eine Schaltfläche auf der grafischen Benutzeroberfläche erstellt. Der Parameter text setzt den auf der Schaltfläche angezeigten Text auf den aktuellen Buchstaben. Der Parameter command legt die Aktion fest, die ausgeführt werden soll, wenn die Schaltfläche angeklickt wird. In diesem Fall handelt es sich um eine Lambda-Funktion, die die Funktion make_guess mit dem aktuellen Buchstaben als Argument aufruft. Die Parameter font und width legen die Schriftart und -breite der Schaltfläche fest. Die Grid-Methode wird verwendet, um die Schaltfläche auf der GUI zu positionieren. Die Zeilen- und Spaltenparameter werden auf der Grundlage des Zählers n berechnet, wodurch die Schaltflächen in einem Raster von 9 Spalten angeordnet werden. Nach der Erstellung und Positionierung jeder Schaltfläche wird der Zähler n um 1 erhöht.
Nach der Schleife wird eine neue Schaltfläche zum Starten eines neuen Spiels erstellt. Der Parameter text setzt den Text der Schaltfläche auf "Neues\nSpiel". Der Befehlsparameter legt die Aktion fest, die ausgeführt werden soll, wenn die Schaltfläche angeklickt wird. In diesem Fall handelt es sich um eine Lambda-Funktion, die die Funktion newGame mit Daten als Argument aufruft. Mit dem Parameter font wird die Schriftart der Schaltfläche festgelegt. Die grid-Methode wird verwendet, um die Schaltfläche auf der GUI zu positionieren. Die Zeilen- und Spaltenparameter werden auf der Grundlage des Zählers n berechnet, so dass die neue Spielschaltfläche direkt hinter den Buchstabenschaltflächen platziert wird.

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
Jeder Beteiligte an dem Projekt hat eine klare Anweisung bekommen, für was er zuständig ist. Dies hat die Gruppe sehr gut erfüllt. Jeder hat einen Teil der Minispielesammlung gemacht. 
z.B. Philipp: Hangman, Robin: TicTacToe und Luis: Schere Stein Papier

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->
![stolz2](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/cd6eea3c-fd19-4b6f-bb41-740e44a21b89)
Der ausgewählte Code ist eine Python-Funktion namens make_guess.

Die Funktion hat einen Parameter, Letter, der der Buchstabe ist, den der Spieler erraten hat. Sie verwendet mehrere globale Variablen: correct_guess, um die Anzahl der richtigen Rateversuche festzuhalten, int_versuche, um die Anzahl der Versuche zu zählen, Underscore_String, um das zu erratende Wort mit Unterstrichen für nicht erratene Buchstaben darzustellen, und Word_with_blanks, um das Wort mit Leerzeichen und richtig erratenen Buchstaben zu speichern.
Die Funktion prüft zunächst, ob die Anzahl der Versuche kleiner als 11 ist. Ist dies der Fall, prüft sie, ob der erratene Buchstabe in dem zu erratenden Wort (Hangman_Word) enthalten ist. Ist der Buchstabe im Wort enthalten, wird jeder Buchstabe des Wortes durchlaufen. Wenn ein Buchstabe des Wortes mit dem erratenen Buchstaben übereinstimmt, wird correct_guess inkrementiert und der entsprechende Unterstrich in Underscore_String durch den erratenen Buchstaben ersetzt. Dann fügt es Underscore_String zu einer Zeichenkette mit Leerzeichen zwischen den Buchstaben zusammen und aktualisiert ein Label (word_label) auf der GUI mit dieser Zeichenkette. Es wird auch eine Version dieser Zeichenkette ohne Leerzeichen (Word_without_blanks) erstellt.

Ist der erratene Buchstabe nicht im Wort enthalten, wird int_versuche inkrementiert und eine Bildbeschriftung (imgLabel) auf der grafischen Benutzeroberfläche mit einem Bild aktualisiert, das der Anzahl der Versuche entspricht.

Nach der Bearbeitung des Versuchs wird geprüft, ob das Wort ohne Leerzeichen gleich dem zu erratenden Wort ist. Wenn dies der Fall ist, wird ein Ton abgespielt und eine Meldung angezeigt, die den Spieler darüber informiert, dass er gewonnen und das Wort richtig erraten hat.

Wenn die Anzahl der Versuche nicht kleiner als 11 ist (d.h. der Spieler hat 11 oder mehr Versuche unternommen), wird eine Meldung angezeigt, dass der Spieler verloren hat und das Wort nicht richtig erraten hat.


## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

<!-- zB -->
<!-- GIT -->
<!-- VSC -->
<!-- Copilot -->
<!-- other -->

![use-of-vs-code(https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/25bfd19e-45a7-4de9-ae57-c691cd15b45c)
Neben diesem Screenshot, haben wir die Gruppe befragt. Diese meinte, dass sie ausschließlich in VS-Code gecoded haben.


## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->
### - Gegenseitiger Support Luis-Vincent
![image](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/153116267/08284e28-ee48-43c7-97c9-0e548ff350e2)
### - Gegenseitiger Support Philipp-Finn
![image](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/153117375/e558db4e-1f38-4ee1-bebc-c3e801b55523)
### - Gegenseitiger Support Robin-Niklas
![Support-Robin-Niklas](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/ad176b58-8256-48b4-862f-39074a818deb)
![Support-Robin-Niklas](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/38a22423-fda9-40b6-879c-6fba058f823d)



# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->
Die Gruppe lernte neben weiter Python Syntax, vor allem das Arbeiten an einem größeren Projekt im Team. Auch das Zeitmanagement spielte eine große Rolle. 
Des Weiteren lernten die Studierenden viel über die Python Library Tkinter.

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->
Neben dem gemeinsamen Arbeiten und verstehen von GIT, gab es ein paar Hürden die es zu überwinden galt. 
Zum Beispiel, wie man das Spielfeld bei TicTacToe schöner gestaltet. 
Dass alle Flächen, an denen ein X oder Kreis gesetzt werden kann gleich groß ist.
![image](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/d1a50da2-8b9a-4580-8b88-ec4ad6dfcacd)

Dies ist der Alte Code:
![ver1](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/12c9ff0f-f51a-4d8f-95fa-2c762193273e)

Und dies der neue:

![ver2](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/d933c956-c9c9-47cc-9071-d178e11909e7)
Es ist kaum eine Veränderung an der Code menge. Aber diese Stellen sind entscheidend, um ein gutes unt strukturiertes Projekt auf die Beine zu stellen.

## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

![data1](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/2d1c5bd8-3a23-4406-b375-03da5b7acd2e)
![data2](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/c32f2b8c-f569-422c-ab6c-c316edc92e74)
![data3](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/98f1dbfa-e71c-4033-ac75-6c491819e90a)
![variable](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/c9913d7e-06c4-4495-9e90-64d91cac0caa)

# - E/A-Operationen und Dateiverarbeitung
### Input:

![input](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/c3e7bede-cc64-428e-9dd4-fb07f39db0b6)

### Output:
![output](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/f300672d-6699-4146-8a5a-1c4f2a977f51)

# - Operatoren
![operator](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/f72204f3-2449-4d2f-985a-a7a2512be06d)


# - Kontrollstrukturen

![if](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/44ae325a-53f7-4b31-b470-838cd2164245)

# - Funktionen

![function](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/402da716-33a0-4d29-8c67-3e4fba2c474d)


# - Stringverarbeitung
![string](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/2e9dcb9e-c5a8-48e0-a63f-26a4ae0b4da1)

# - Strukturierte Datentypen

![list](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/c590f615-aaf0-42c6-a03e-689b1f17735a)
