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
// show div if it hide 
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
// add blure efect 
function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return {
      left: rect.left + window.scrollX,
      top: rect.top + window.scrollY
    };
  }
// get pos of in el
  function qt(e , number ,tid){
    price = document.getElementById(tid)
    nprice = parseFloat(number).toFixed(2);
    tprice = e*nprice
    price.value = tprice.toFixed(2)

    prices = document.getElementsByClassName('price')
    total = 0.0
    Array.from(prices).forEach((i)=>{
      total += parseFloat(i.value)
   })
   sum = 0.0
   document.getElementById('items').innerHTML = total+" IQD"
   shipping = document.getElementsByClassName('shipping')
   Array.from(shipping).forEach((e)=>{
    if(shipping.length <= 1){
      sum = total + parseFloat(e.innerHTML) 
    }else{
      if(e.checked){
        sum = total +parseFloat(e.value)
      }
    }
   })
   document.getElementById('total').innerHTML = sum
}
// clc total price and replace it 

function add(id , price ,to){
  main = document.getElementById(id)
  main.value++
  qt(main.value,price , to)
}
function sub(id , price ,to){
  main = document.getElementById(id)
  if (main.value != 0){
      main.value--;
  }
  qt(main.value , price, to)
}
// two btns for add sub the qt in orderds 
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
// get items ready to buy if the user not loged in or not have cart 



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
// finish the bay method 


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
// for any larg data 
//  end of show more function
hidflag = true
// controll the nav bar 
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
// moving the lime -> to controll the animation on the main page 
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

numfex = document.getElementsByClassName('numfex')
Array.from(numfex).forEach((i)=>{
  number = parseFloat(i.innerHTML).toFixed(2)
  i.innerHTML = number
})

// function slowhidenav(){
//   console.log('hi')
//   let start = window.pageYOffset;
//   main = document.getElementById('nv')
//   let scroller = $("#popup").position().top;
//   console.log(start , scroller)
  
// }
// document.getElementById('popup').addEventListener('scroll',slowhidenav)



function deletes(){
  data=[]
  selected = document.getElementsByClassName('selected')
  Array.from(selected).forEach((i)=>{
      if(i.checked){
          list = i.value.split(',')
          data.push(list)
      }
  })
  data.forEach((e,index)=>{
          
              infl = data[index][0]
              list = data[index][1]
              $.ajax({
                  type:'get',
                  url:`deleteFromList/${list},${infl}`,
                  data: {
                      'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
                  },success:()=>{
                      location.reload();
                  }
              })
          
  })
}

function request(){
  data=[]
selected = document.getElementsByClassName('selected')
Array.from(selected).forEach((i)=>{
  if(i.checked){
      list = i.value.split(',')
      data.push(list)
  }
})
data.forEach((e,index)=>{

  infl = data[index][0]
  list = data[index][1]
  $.ajax({
      type:'POST',
      url:`RequestInfluncer`,
      data: {
          'id':infl,
          'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      },success:()=>{
          location.reload();
      }
  })

})
}
// ajax request to selected items


if(document.getElementById('aside')){
  main = document.querySelector('.actions')
  lis = main.querySelectorAll('li')
  Array.from(lis).forEach((e)=>{
    e.addEventListener('click' , ()=>{
      Array.from(lis).forEach((e)=>{
        if(e.classList.contains('clicked')){
          e.classList.remove('clicked')
        }
      })
    })
  })
  
  
  
  Array.from(lis).forEach((e)=>{
    e.addEventListener('click' , ()=>{
      e.classList.add('clicked')
    })
  })
}
// aside moving 
// to change the image size in edite logo page 

function imagesize(id){
  var dataurl
  image = document.getElementById(id)
  input = document.getElementById('range')
  if(input.value < 50){
    input.value = 50
  }else if(input.value > 150){
    input.value = 150
  }
  // image.style.width = input.value + "px"
  // image.style.height = input.value + "px"
  input.oninput = function(){
    const canv = document.createElement('canvas')
    const ctx = canv.getContext('2d')
    canv.width = input.value
    canv.height = input.value
    
    ctx.drawImage(image ,0 ,0)
    var dataurl = canv.toDataURL('image/jpeg' , 1.0)
    image.src = dataurl
    
    

    input.onchange = function(){
      setTimeout(() => {
        // console.log(image , image.files[0])
        img = image.files
  
        const formData = new FormData()
        formData.append('logo', dataurl)
        console.log(img , dataurl)
        $.ajax({
          url: '/log',
          type: 'POST',
          data: formData,
          processData: false,
          contentType: false,
          headers: {
            'X-CSRFToken': $('#form input[name=csrfmiddlewaretoken]').val(),
          },
          success: function(response) {
            console.log('Image uploaded successfully');
          },
          error: function(xhr, status, error) {
            console.error(error);
          },
        });
        console.log("done")
      }, 1000);
    }

  }

  
}

// resizeing the image and save it in db 
