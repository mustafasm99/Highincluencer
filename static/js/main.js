counter = 1
function show(id){
    x = document.getElementById(id);
    if(counter === 1){
        x.style = "display:block;";
        counter --;
    }
    else{
        x.style = "display:none;";
        counter++;
    }
    
}

function fade(element) {
    var op = 1;  // initial opacity
    var timer = setInterval(function () {
        if (op <= 0.1){
            clearInterval(timer);
            element.style.display = 'none';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
    }, 50);
}

function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return {
      left: rect.left + window.scrollX,
      top: rect.top + window.scrollY
    };
  }
  
  function add(id){
   document.getElementById(id).value++
  }
  function sub(id){
    if (document.getElementById(id).value != 0){
        document.getElementById(id).value--;
    }
  }
  
  function baynowx(){
    items = document.getElementsByClassName('selected');
    sitems = document.getElementById('sitems');
    Array.from(items).forEach(el=>{
      el.classList.add('items');
      sitems.appendChild(el);
      // el.classList.remove('selected');
      el.style=`
      overflow-y: scroll;
      `
      div = document.createElement('div');
      el.appendChild(div);
      input = document.createElement("input");
      input.type = "hidden";
      input.name = "item";
      input.value = el.id;
      el.appendChild(input)

      input = document.createElement('input');
      input.type = "number";
      input.min = "0";
      input.placeholder = "Quantity";
      input.name = "qt";
      input.id = "qt";
      div.appendChild(input);      
    })
  }



function baynow(){
  x = document.getElementsByClassName('qtInput')
  y = document.getElementById('form')
  Array.from(x).forEach(i=>{
    input = document.createElement('input')
    input.type="hidden"
    input.name="qt"
    input.value=i.value
    y.appendChild(input)
  })
}
// slider 


// for table numbers 
function clcnumbers(arrayofEl){
    data = Array.from(arrayofEl).forEach((e,i)=>{
    currentDay = parseFloat(e.innerHTML);
    next = i+1
    if(next == arrayofEl.length){
      nextday = parseFloat(arrayofEl[i].innerHTML)
    }
    else{
      nextday = parseFloat(arrayofEl[next].innerHTML)
    }
  
    x = parseFloat(currentDay)-parseFloat(nextday)
    if (x%1 !== 0)
    {
      x = x.toFixed(2)
    }
    if(x > 0){
      e.innerHTML =`<div class="tablenot">
      <span>
      ${currentDay}
      <p class="incfl">
        +${x}
      </p>
      </span>
      </div>` 
    }
    else if(x == 0){
      
    }
    else{
      e.innerHTML =`
        <div class="tablenot">
        <span>
        ${currentDay}
        <p class="decfl">
          ${x}
        </p>
        </span>
        </div>
      `;
    }  
  })
}


// end for tables 
showflag = true
function showmore(id,cx,showmorebtn){
  if(showflag){
    btn = document.getElementById(showmorebtn);
    x = document.getElementById(id);
    x.classList.remove(cx);
    btn.innerHTML = "See Less";
    showflag = false;
  }
  else{
    x.classList.add(cx)
    btn.innerHTML = "See more"
    showflag = true
  }
  
}

//  end of show more function
hidflag = true

function Move(){
  sectionsel = document.querySelectorAll('section')
  mainnav = document.getElementById('nv')
  if(mainnav.classList.contains('nvmoveBack')){
    mainnav.classList.remove('nvmoveBack');
  }
    mainnav.classList.add('nvmove')
  Array.from(sectionsel).forEach((e)=>{
    if(e.classList.contains('mainMoveBack')){
      e.classList.remove('mainMoveBack');
    }
    e.classList.add('mainMove')
  })
}
function Back(){
  Array.from(sectionsel).forEach((e)=>{
    e.classList.remove('mainMove');
    e.classList.add('mainMoveBack');
  })
  mainnav.classList.remove('nvmove');
  mainnav.classList.add('nvmoveBack');

}
// moving the lime 
function linemove(){
  lines = document.querySelectorAll('.center_to_first');
  Array.from(lines).forEach((e)=>{
    if (e.classList.contains('lineanimeBack')){
      e.classList.remove('lineanimeBack')
    }
    e.classList.remove('center_to_firset')
    e.classList.add('lineanime')
  })
}

function linemoveBack(){
  lines = document.querySelectorAll('.center_to_first');
  Array.from(lines).forEach((e)=>{
    e.classList.remove('center_to_firset')
    e.classList.remove('lineanime')
    e.classList.add('lineanimeBack')
  })
}
//end of moving the line 
function hid(id,btn,flag){
  main = document.getElementById(id);
  btn = document.getElementById(btn);
  
    
  
  // fucntion tase start Hear

  if(hidflag){
    // Start Hidding //
    // linemove()
    // Move()
    if(main.classList.contains('hid2')){
      main.classList.remove('hid2');
      btn.classList.remove('hidbtn2');

      // body.classList.add('biger');
    }
    main.classList.add('hid');
    btn.classList.add('hidbtn');

    // flag using to recgnise any actions for true it moving icons 
    if(flag){
      icon = document.getElementsByClassName('iconeImgHolder')
      flagsection = document.getElementById('dspage')
      // for  the hole section 
      if (flagsection.classList.contains('sectionAnB')){ // the Animation class for influencer descovery page backwoards 
        flagsection.classList.remove('sectionAnB')
        flagsection.classList.add('sectionAn') // the Animation class for influencer descovery page forwoards
      }else{
        flagsection.classList.add('sectionAn')
      }

      //for the icons 
      Array.from(icon).forEach((e)=>{
        if(e.classList.contains('iconAnB')){
          e.classList.remove('iconAnB')
        }
        e.classList.add('iconAn')
      })
    }

    hidflag = false
  }
  // Back
  else{
    // linemoveBack()
    // Back()
    main.classList.remove('hid');
    btn.classList.remove('hidbtn');
    main.classList.add('hid2');
    btn.classList.add('hidbtn2');

    // flag using to recgnise any actions for true it moving icons //
    if(flag){
      flagsection = document.getElementById('dspage')
      if (flagsection.classList.contains('sectionAnB')){
        flagsection.classList.remove('sectionAnB')
      }else{
        flagsection.classList.add('sectionAnB')
      }

      icon = document.getElementsByClassName('iconeImgHolder')
      Array.from(icon).forEach((e)=>{
        if(e.classList.contains('iconAn')){
          e.classList.remove('iconAn')
        }
        e.classList.add('iconAnB')
      })
    }


    hidflag = true;
  }
 

}

// hide nav bar

function hidtoolib(){
  document.getElementById('popup').remove();
  document.querySelector('#gridHolder').style.filter = 'blur(0px)'
}


var animLeft = 0;
function left(){
  animLeft+=10
  main = document.getElementById('mainscroller').scrollLeft +=animLeft;
}

function right(){
  main = document.getElementsByClassName('sgholder')
  each = Array.from(main).forEach((i)=>{
    width = i.offsetWidth;
    cuurentleft = main[0].offsetLeft;
    i.animate([
    {
      left:`${cuurentleft}px`
    },{
        left:'150px'
      }
    ],{
      duration:700,
      fill:'both',
      easing:'ease-in-out'
    })
  })
}


function showcapzk(e,text){
  newh = Math.floor(((e+2)*text)*140)
  x = document.getElementById('postsRecent').style = "height:"+newh+'px'
}

// window.onscroll = function(){
//   section = Array.from(document.querySelectorAll('section'))
//   lists = Array.from(document.getElementsByClassName('nvbartag'))

  
// }
acv = document.getElementsByClassName('nvbartag');
Array.from(acv).forEach((item)=>{
  item.addEventListener('click',()=>{
    Array.from(acv).forEach((i)=>{
      if(i.classList.contains('active')){
        i.classList.remove('active')
      }
    })
  item.classList.add('active')
  })
})

function lineChar(ele,name,data,dataNames,backColor,borderColor){
  temp=[]
  dataNames.forEach((e)=>{
    if (temp.length > 1){
      if(temp[0].slice(0,4) == temp[1].slice(0,4)){
          temp.push(e.slice(5))
      }
      else{
          temp.push(e)
      }
  }else{
      temp.push(e)
  }
  })
  
   let charx = new Chart(ele,{
    type:'line',
    data:{
      labels:temp,
      datasets:[{
        label:name,
        data:data,
        backgroundColor:backColor,
        borderColor:borderColor,
        tension:0.2,
      }],
    },
    options:{
      responsive:true,
      plugins: {
        legend: {
          display: false
        }
      }
  }     
   })
}

function doughnutChart(ele,name,data1,data2,firstColor,secondColor,height,width){ // doughnut chart function
  let doughnut = new Chart(ele,{
    type:'doughnut',
    data:{
        labels:name,
        datasets:[{
            // label:'Followers',
            data:[data1,data2],
            backgroundColor:[firstColor,secondColor],
        }]
    },
    options:{
      responsive:true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      }
  }   
  })
}

// spceital chart function



// number orgnization 

numx = document.getElementsByClassName('numx')
ar = Array.from(numx).forEach((i)=>{
  number = parseFloat(i.innerHTML)
    if (number > 1000){
      i.innerHTML = ``+Math.floor(number/1000)+'K'
    }
    else if(number > 1000000){
      i.innerHTML = ``+Math.floor(number/1000000)+'M'
    }
})


// function slowhidenav(){
//   console.log('hi')
//   let start = window.pageYOffset;
//   main = document.getElementById('nv')
//   let scroller = $("#popup").position().top;
//   console.log(start , scroller)
  
// }
// document.getElementById('popup').addEventListener('scroll',slowhidenav)
