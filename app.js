(function(){
    var firebaseConfig = {
        apiKey: "AIzaSyDTZ08oeMMWDRH1wfNaejAwt3ZJ5gNQuEY",
        authDomain: "igdtuw-hacks.firebaseapp.com",
        databaseURL: "https://igdtuw-hacks.firebaseio.com",
        projectId: "igdtuw-hacks",
        storageBucket: "igdtuw-hacks.appspot.com",
        messagingSenderId: "242275361121",
        appId: "1:242275361121:web:fc903c8aa2762474"
  };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    
    
    const email=document.getElementById("email");
    const pass=document.getElementById("pass");
    const submitbtn=document.getElementById("submitbtn");
    
    submitbtn.addEventListener('click', e =>{
        const email=email.nodeValue;
        const pass= pass.nodeValue;
        const auth= firebase.auth();
        
        const promise= auth.createUserWithEmailAndPassword(email,pass);
    });
    
    firebase.auth().onAuthStateChanged(firebaseUser =>{
        if(firebaseUser){
            console.log(firebaseUser);
        } else{
            console.log('Not logged in!');
        }
    });

})()



    