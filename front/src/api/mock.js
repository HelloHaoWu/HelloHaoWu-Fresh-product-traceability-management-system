import Mock from 'mockjs'
import homeApi from './mockData/home.js'//这一行引入export的方法，拦截的数据要渲染成其中的对象列表


Mock.mock('/home/getData',homeApi.getHomeData)//这是拦截数据的一行，拦截第一个参数的数据，变相为第二个参数（一个方法）返回的数据