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
         cosnole.log(burger)
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

      } else {
         console.log("Width > 1280px");
      }
   }

   qDesktop();
};

function updating_cart() {
   let updateBtns = document.querySelectorAll(".update-cart")

   for(let i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener("click", function() {
       print("Test")
      let productId = this.dataset.product
      let action = this.dataset.action
      console.log("ProductId", productId, "Action", action)

      if(user === "AnonymousUser"){
         console.log("Not logged in")
      }
      else{
         updateUserOrder(productId, action)
        }
    })
    }

    function updateUserOrder(productId, action){
      console.log("User is logged in, sending data...")

      let url = "/update_item/"

      fetch(url, {
         method: "POST",
         headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
         },
         body: JSON.stringify({"productId": productId, "action": action})
      })
      .then((response) => {
         return response.json()
      })
      .then((data) => {
         console.log("Data", data)
         location.reload()
      })
   }
}

function search() {
   // Search bar
   const search = document.querySelector(".search-bar");
   const cross = document.querySelector(".delete");

   search.addEventListener("click", () => {
      search.classList.toggle("search-hover");
      cross.classList.toggle("cross-hover");
   });

   cross.addEventListener("click", () => {
      search.value = "";
      search.classList.remove("search-hover");
      cross.classList.remove("cross-hover");
   });
}

search()

updating_cart()

cont()