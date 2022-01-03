from random import randint
print("""                                                                                         
                                                                                          
                                     '''''^,,,,,,,,,''''                                  
                          .`,![tt$$$$$$$$vttttttttttt$$$$$*t!,'                           
                      'I|M&x|?,,"'''                    .'^,?|zM|I.                       
                    'n$?^.                                     .^1$M"                     
                   .W$`                                           .[$[                    
                   x$'                                              I$x.                  
                  ?$?                                                !$<                  
                  $$"                                                 *$                  
                 `$$        '`,,,,'.                    ''''''.       ,$!                 
                 :$x    ^!z$Mz|?xx$$$xI.           .^1M$$Mxxxx&$x<.    $M                 
                 1$!  .tj!` !W$*1,."t$$$[.        !$$$t!![tv$t..,-*[.  $$                 
                 1$!  ^.      .^I|Mx!^IM$*      .x$M??|$&?,.       ',  1$,                
                 n$^               "|$x^..       ''!M&!^               1$!                
                 $$                  ,W$*'        t*,.                 1$!                
                 $$       "??xx???!,'.`$$z.      ?,    ',??xxx1!^      1$!                
                 $$    .|M$$$$$$$$$$$$1?$$!        .!n$$$$$$$$$$$x^.   1$!                
                 $$  `$$$$$$$$$$$$$$$$i!$$t        ,*$$$$$$$$$$$$Wtt-,`)$!                
                 $$  '?,,,,,,,,,,,^'.  !$$$                            x$,                
                 1$!                   !$$$                            $$                 
                 -$$.                  !$$$                           `$*                 
                 "$$/.                 |$$$                           ?$!                 
                  $$$M,              ^/$$$?                         '|$8                  
                  !$vt$v!``     `` '*$$$$$!       :[.            .,t$$$-                  
                   M$'?$$$$M?I,,`. 1$M'|$$.        .x'  .,,,,?/xM/$$x$$'                  
                   '$M.<$|$$?.     `M, x$x           .      .!$$,I$?x$!                   
                    ?$t !$:$$W,.       [$1                 `*$$`.W!!$t                    
                    .$$, 'z,!$$$/!^'  .,$$!,,,,/$M'     `!M$$M`!$,,$z.                    
                     '$&' .||"!M$$$$$$$$$$$M<M$$$$$M?/M$$$$x^^xx'`$$'                     
                      `$*.  !W,.'!t$$$$$$$>   ,W$$$$$$$$v!.`*$1 .W$,                      
                       ,$M.  ?$$?^  '^,,,I,,,,,I?????,'.   `M! 'M$^                       
                        ,$z.  ,$$$x?,^.                   ^/. `$$"                        
                         `$*`  `$$,  `!,!!!!!!!!!        !t. `W$`                         
                          "$$"  ,$!      .$$$$$z.       ,^  !$z.                          
                           'x$?. ^M.      x$$$$"       .. ./$|.                           
                             1$*' ..     :$$$$$)         ,$$,                             
                              :M&!       1$$$$$$,      .1$M'                              
                                ?$M,     I$$$$$x     .|$*^                                
                                 .[$*,   .$$$$$:   .[W$[.                                 
                                   '|$z!' ?$$$$`.^1$M?.                                   
                                     .,|$&M$$$$z$M?^                                      
                                         `!!!!!".                                         
                                                                                          
                                                                                          """)
print() 
print("                    *************************************************")
print("                    *       GITHUB => GHOSTEPROG                    *")
print("                    *       INSTAGRAM => @GHOSTEPROG                *")
print("                    *************************************************")
print()
Name = input("Name: ")
Last_name = input("Last Name >  ")
Birth_year = input("Birth Year >  ")
Age_target = input("Age target >  ")
Phone_Number = input("Phone Number >  ")
National_Id = input("NAtional_Id >  ")
Fother_Name = input("Fother Name >  ")
Fother_Age = input("Fother Age >  ")
Mother_Name = input("Mother_Name >  ")
Mother_Age = input("Age Mother >  ")
words = [Name, Last_name, Birth_year, Age_target, National_Id, Phone_Number, Fother_Name, Fother_Age, Mother_Name, Mother_Age]
random_passwords = []
for word1 in words:
    for word2 in words:
        random_passwords.append(word1 + word2)

for word1 in words:
    for word2 in words:
        random_passwords.append(word1 + word2)
        for char in ["@", "#", "$", "%", "*", "&", "^", "!", "~"]:
            random_passwords.append(word1 + char + word2)

for word1 in words:
    for word2 in words:
        for word3 in words:
            random_passwords.append(word1 + word2 + word3)
            for char in ["123", "1234", "12345", "123456", "1234567", "12345678", "123456789"]:
                random_passwords.append(word1 + char + word2 + char + word3)
                random_passwords.append(word1 + char + word2 + word3)
                random_passwords.append(word1 + word2 + char + word3)

for word1 in words:
    for word2 in words:
        for word3 in words:
            for word4 in words:
                random_passwords.append(word1 + word2 + word3 + word4)
                for char in ["1122", "112233", "112233", "1122334455", "112233445566", "11223344556677"]:
                    random_passwords.append(word1 + char + word2 + char + word3 + char + word4)
                    random_passwords.append(word1 + char + word2 + word3 + word4)
                    random_passwords.append(word1 + word2 + char + word3 + char + word4)

with open("Password.txt", "w") as file:
    for password in random_passwords:
        file.write(password + "\n") 
    print()
    print("|*| Creact File Txt Name Password.txt :)")
