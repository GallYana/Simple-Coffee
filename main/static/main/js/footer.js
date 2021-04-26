function footer(){
    var
        main = document.getElementsByTagName('main')[0],
        footer = document.getElementsByTagName('footer')[0];
    
        footerHeight = footer.clientHeight;
        main.style.paddingBottom = (footerHeight)+'px';
    }
    window.addEventListener('load',footer);
    window.addEventListener('resize',footer);