import{_ as k,m as f,r as u,o as d,c as v,a as e,b as s,w as o,d as h,e as m,f as g}from"./index-38b3b81d.js";import{useUserStore as b}from"./login-a476a6d2.js";const y={name:"SelfAside",components:{Menu:f},data(){return{user:b().user}},mounted(){console.log(this.user);const i=document.querySelectorAll(".nav_link");function _(){i.forEach(t=>t.classList.remove("active")),this.classList.add("active")}i.forEach(t=>t.addEventListener("click",_));const r=document.getElementsByClassName("collapse__link");var l;for(l=0;l<r.length;l++)r[l].addEventListener("click",function(){const t=this.nextElementSibling;t.classList.toggle("showCollapse"),t.previousElementSibling.classList.toggle("rotate")})},methods:{showMenu(i,_,r){const l=document.getElementById(i),t=document.getElementById(_),c=document.getElementById(r);if(l&&t){t.classList.toggle("expander"),c.classList.toggle("body-pd");const n=document.getElementById("collapselink");n.nextElementSibling.classList.toggle("showCollapse")==!0&&n.nextElementSibling.classList.toggle("showCollapse"),n.classList.toggle("rotate")==!0&&n.classList.toggle("rotate")}},show_customerpage(){return this.user==="customer"||this.user==="manager"},show_dispatcherpage(){return this.user==="dispatcher"||this.user==="manager"},show_managerpage(){return this.user==="manager"}}},w={id:"body-pd"},E={class:"l-navbar",id:"navbar"},L={class:"nav"},C={class:"nav_brand"},x=e("a",{class:"nav_logo"},"生鲜管理系统",-1),B={class:"nav__list"},S=e("span",{class:"nav_name"},"主页",-1),N=e("span",{class:"nav_name"},"客户",-1),A=e("span",{class:"nav__name"},"配送",-1),I={key:2,class:"nav_link collapse"},M=e("span",{class:"nav__name"},"管理",-1),V={class:"collapse_menu"},q=e("br",null,null,-1),T=e("br",null,null,-1),U=e("br",null,null,-1),$=e("span",{class:"nav_name"},"设置",-1),j=e("span",{class:"nav_name"},"退出登录",-1),z={class:"right-side"};function D(i,_,r,l,t,c){const n=u("ion-icon"),a=u("router-link"),p=u("router-view");return d(),v("body",w,[e("div",E,[e("nav",L,[e("div",null,[e("div",C,[s(n,{name:"menu-outline",class:"nav_toggle",id:"nav_toggle",onClick:_[0]||(_[0]=F=>c.showMenu("nav_toggle","navbar","body-pd"))}),x]),e("div",B,[s(a,{to:"/home",class:"nav_link active"},{default:o(()=>[s(n,{name:"home-outline",class:"nav_icon"}),S]),_:1}),c.show_customerpage()?(d(),h(a,{key:0,to:"/customer",class:"nav_link"},{default:o(()=>[s(n,{name:"person-outline",class:"nav_icon"}),N]),_:1})):m("",!0),c.show_dispatcherpage()?(d(),h(a,{key:1,to:"/deliver",class:"nav_link"},{default:o(()=>[s(n,{name:"analytics-outline",class:"nav_icon"}),A]),_:1})):m("",!0),c.show_managerpage()?(d(),v("div",I,[s(n,{name:"layers-outline",class:"nav_icon"}),M,s(n,{id:"collapselink",name:"chevron-down-outline",class:"collapse__link"}),e("ul",V,[s(a,{to:"/manage-1",class:"collapse__sublink"},{default:o(()=>[g("统计面板"),q]),_:1}),s(a,{to:"/manage-2",class:"collapse__sublink"},{default:o(()=>[g("订单详览"),T]),_:1}),s(a,{to:"/manage-3",class:"collapse__sublink"},{default:o(()=>[g("库存总览"),U]),_:1})])])):m("",!0),s(a,{to:"/settings",class:"nav_link"},{default:o(()=>[s(n,{name:"settings-outline",class:"nav_icon"}),$]),_:1})])]),s(a,{to:"/",class:"nav_link"},{default:o(()=>[s(n,{name:"log-out-outline",class:"nav_icon"}),j]),_:1})])]),e("div",z,[s(p)])])}const J=k(y,[["render",D]]);export{J as default};
