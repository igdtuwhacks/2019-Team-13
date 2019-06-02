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
    
    
    const preobject=document.getElementById("object");
    const ulist=document.getElementById("list");
    
    //create referrence
    
    const dbRefObject=firebase.database().ref().child('object');
    const dbRefList=dbRefObject.child('hobbies')
;    
    //sync
    
    dbRefObject.on('value' , snap =>{
        preobject.innerText = JSON.stringify(snap.val(), null, 3);
    } );
    
    dbRefList.on('child_added', snap =>{
        const li=document.createElement('li');
        li.innerText=snap.val();
        li.id=snap.key;
        ulist.appendChild(li);
    }); 
    
    dbRefList.on('child_changed', snap =>{
        const lichnaged=document.getElementById(snap.key);
        lichanged.innerText=snap.val();
    });

    
    dbRefList.on("child_removed", snap =>{
        const liToRemove=document.getElementById(snap.key);
        lichanged.innerText=snap.val();
    })
})();