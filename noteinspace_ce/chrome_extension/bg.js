
var THE_NAME = 'noteinspace';
var contextsSupported = ["link", "selection"];
var host = 'http://127.0.0.1:5007/api'

function onClickHandler(info, tab) {
	var	postdata = {
        'source': info['pageUrl']
	}
	//console.log(info, tab)
	var clickSource = info.menuItemId;
	if(clickSource == "linkToGroup"){
		postdata['type'] = 'link';
		postdata['content'] = info['linkUrl'];
	} 
	if(clickSource == "selectionToGroup"){
		postdata['type'] = 'selection';
		postdata['content'] = info['selectionText'];
	}
	//console.log(postdata);
	
	var xhr = new XMLHttpRequest();
	var url = host+'/notes'
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-type", "application/json");
	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4 && xhr.status === 201) {
			chrome.browserAction.setBadgeBackgroundColor({color:[0, 255, 0, 230]});
			var json = JSON.parse(xhr.responseText);
			console.log(json);
			console.log(xhr.responseText);
		}
		else{
			chrome.browserAction.setBadgeBackgroundColor({color:[255, 0, 0, 230]});
			console.log('op failed');
		}
	};
	xhr.send(JSON.stringify(postdata));
};

chrome.contextMenus.onClicked.addListener(onClickHandler);
chrome.browserAction.setBadgeBackgroundColor({color:[170, 170, 170, 230]});
chrome.browserAction.setBadgeText({text:"NIS"});

//rightclick context menu
chrome.runtime.onInstalled.addListener(function() {
	chrome.contextMenus.create({"title": THE_NAME, "contexts": contextsSupported,"id": "rootcon"});
	for (var i=0, l=contextsSupported.length; i<l; i++) {
		chrome.contextMenus.create(
			{"title": 'save as '+contextsSupported[i], 
				"parentId": "rootcon", "contexts":[contextsSupported[i]], "id": contextsSupported[i]+"ToGroup"});
	}
});


