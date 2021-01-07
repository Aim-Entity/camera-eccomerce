function cont() {
   function qMobile() { // Mobile query
      let mediaMobile = window.matchMedia("(max-width: 376px)")
      
      if (mediaMobile.matches) {

         // Nav => solid background
         const nav = document.querySelector(".nav");
   
         window.addEventListener("scroll", () => {
            let windowPosition = window.scrollY > 0;
            nav.classList.toggle("scroll-nav", windowPosition);
         });
   
         // Nav - burger
         const burger = document.querySelector(".burger-menu");
         const burgerMenu = document.querySelector(".nav-menu");
   
         burger.addEventListener("click", () => {
            burger.classList.toggle("burger-open");
            burgerMenu.classList.toggle("openM");
   
            if (burger.classList !== "burger-open") {
               productsMenu.classList.remove("products-open");
            }
   
            if (window.scrollY < 1) {
               nav.classList.toggle("scroll-nav");
            }
         });
   
         // Nav - products
         const products = document.querySelector(".link-products");
         const productsMenu = document.querySelector(".nav-products")
   
         products.addEventListener("click", () => {
            productsMenu.classList.toggle("products-open");
         });
   
         const goBack = document.querySelector(".nav-back");
   
         goBack.addEventListener("click", () => {
            productsMenu.classList.remove("products-open");
         });
   
         // Sign in
         const signIn = document.querySelector(".sign-in");
         const signInLink = document.getElementById("sign-in-link");
         const signInBack = document.querySelector(".sign-in-back");
         const signUpBtn = document.querySelector(".sign-ing-button");
         const signUp = document.querySelector(".sign-up2");
         const signUpBack = document.querySelector(".sign-up-back");
         const signInButton = document.querySelector(".sign-up-button");
   
         signInLink.addEventListener("click", () => {
            signIn.classList.toggle("sign-in-active");
         });
   
         signInBack.addEventListener("click", () => {
            signIn.classList.remove("sign-in-active");
         });
   
         signUpBtn.addEventListener("click", () => {
            signUp.classList.add("sign-up-active");
            signIn.classList.remove("sign-in-active");
         });
   
         signUpBack.addEventListener("click", () => {
            signUp.classList.remove("sign-up-active");
         });
         
         signInButton.addEventListener("click", () => {
            signIn.classList.add("sign-in-active");
            signUp.classList.remove("sign-up-active");
         });

      } else {
         console.log("Width > 375px");
      }
   }

   qMobile();

   function qDesktop() { // Media query for desktop
      let mediaDesktop = window.matchMedia("(min-width: 1025px)");
      let mediaDesktop2 = window.matchMedia("(max-width: 1280px)");

      if (mediaDesktop.matches && mediaDesktop2.matches) {

         // Nav - background
         const navD = document.querySelector(".nav-b");
   
         window.addEventListener("scroll", () => {
            let windowPositionD = window.scrollY > 0;
            navD.classList.toggle("nav-b-active", windowPositionD);
         });

         // Sign in
         const signIn = document.querySelector(".sign-in");
         const signInLink = document.getElementById("sign-in-link");
         const signInImg = document.querySelector(".account-img");
         const signInBack = document.querySelector(".sign-in-back");
         const signUpBtn = document.querySelector(".sign-ing-button");
         const signUp = document.querySelector(".sign-up2");
         const signUpBack = document.querySelector(".sign-up-back");
         const signInButton = document.querySelector(".sign-up-button");

         signInLink.addEventListener("click", () => {
            signIn.classList.toggle("sign-in-active");
         });

         signInImg.addEventListener("click", () => {
            signIn.classList.toggle("sign-in-active");
         });

         signInBack.addEventListener("click", () => {
            signIn.classList.remove("sign-in-active");
         });

         signUpBtn.addEventListener("click", () => {
            signUp.classList.add("sign-up-active");
            signIn.classList.remove("sign-in-active");
         });

         signUpBack.addEventListener("click", () => {
            signUp.classList.remove("sign-up-active");
         });

         signInButton.addEventListener("click", () => {
            signIn.classList.add("sign-in-active");
            signUp.classList.remove("sign-up-active");
         });

         // Lp - link
         const productLink1 = document.querySelector(".lp-p-link1");
         const productArrow1 = document.querySelector(".lp-p-goto1");
         const productLink2 = document.querySelector(".lp-p-link2");
         const productArrow2 = document.querySelector(".lp-p-goto2");

         productLink1.addEventListener("mouseover", () => {
            productArrow1.style.transform = "translateX(0.5rem)";
            productArrow1.style.transition = "ease 400ms";
         });
         
         productLink1.addEventListener("mouseout", () => {
            productArrow1.style.transform = "translateX(0rem)";
            productArrow1.style.transition = "ease 400ms";
         });

         productLink2.addEventListener("mouseover", () => {
            productArrow2.style.transform = "translateX(0.5rem)";
            productArrow2.style.transition = "ease 400ms";
         });
         
         productLink2.addEventListener("mouseout", () => {
            productArrow2.style.transform = "translateX(0rem)";
            productArrow2.style.transition = "ease 400ms";
         });

      } else {
         console.log("Width > 1280px");
      }
   }

   qDesktop();
};

cont()