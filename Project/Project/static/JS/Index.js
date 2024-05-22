function ToggleFilter() 
{
    var FilterList = document.getElementById("filterList");
    if (FilterList.style.height === "0px") 
    {
        FilterList.style.height = "252.9px";
    } 
    else 
    {
        FilterList.style.height = "0px";
    }
}

function hide()
{
    document.getElementById("textt").style.display = "none";
}
