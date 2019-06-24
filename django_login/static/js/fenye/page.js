let Option = {
    url: 'http://127.0.0.1:8000/xiaoque/get_xiaoque/?pageIndex=',//请求地址
    methods: 'get',//请求方法
    index: 1,//默认起始页
    data:[],
    total:0
};

let ajax = function (methods, url, params, callback) {//ajax请求函数
    let xhr = new XMLHttpRequest(),data;
    if (methods == '' && url == '') {
        console.error('Ajax need some agreements seems you lose');
        return ''
    }
    if (methods.toLocaleLowerCase() === 'get') {
        xhr.open('get', url);
        xhr.send()
    } else if (methods.toLocaleLowerCase() === 'post') {
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.open('get', url);
        xhr.send(params)
    }
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let result =  JSON.parse(xhr.responseText);
            fenyeList(result.result.total);
            Option.total = result.result.total;
            Option.data = result.result.data
        }
    }

}
let xhrdata = function (pageIndex) {//请求数据
    return ajax(Option.methods,Option.url += pageIndex)
}
let fenyeList = function(total){
    let fenYe = [];//分页页面渲染
    let box = document.querySelector('#box');
    box.innerHTML='';
    let perv = document.createElement('span');//上一页
    perv.className = 'perv';
    perv.textContent = '<';
    fenYe.push(perv);

    for (let i = 1; i <  total + 1; i++) {
        let span = document.createElement('span');
        span.textContent = i + '';
        fenYe.push(span)
    }

    let next = document.createElement('span');//下一页
    next.className = 'next';
    next.textContent = '>';
    fenYe.push(next);


    for (let i = 0, len = fenYe.length; i < len; i++) {//渲染分页页面
        box.appendChild(fenYe[i])
    }
};
xhrdata(Option.index);

//事件委派
box.addEventListener('click', (e) => {
    e = e || event;
    let index, target = e.target;
    let nodes = target.parentNode.children,
        len = nodes.length,
        total = Option.total;
    if (target.nodeName !== 'SPAN') {
        return
    }
    if (target.textContent == '<') {
        index = Option.index - 1;
        if (index < 0) {
            index = 0
        } else {
            nodes[index + 1].classList += 'active';
            nodes[index + 2].classList.remove('active')
        }
        Option.index = index
    } else if (target.textContent == '>') {
        index = Option.index + 1;
        if (index > total - 1) {
            index = total - 1
        } else {
            nodes[index + 1].classList += 'active';
            nodes[index].classList.remove('active')
        }
        Option.index = index
    } else {
        for (let i = 0; i < len; i++) {
            if (nodes[i].classList == undefined) {
                continue
            }
            nodes[i].classList.contains('active') ?
                nodes[i].classList.remove('active') : null
        }
        target.className += ' active ';
        index = target.textContent - 1;
        Option.index = index
    }
    xhrdata(Option.index );
    datarefresh(Option.data)

});
//数据渲染函数
let datarefresh = function (data) {
    let datacontainer = document.querySelector('#data');

    datacontainer.innerHTML = JSON.stringify(data)
};
