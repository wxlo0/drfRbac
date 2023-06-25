import axios from 'axios'
import qs from 'qs'
import {message} from "ant-design-vue";
import router from "@/router";
import store from "@/store";

const http = axios.create({
    timeout: 30 * 60 * 1000,
    baseURL: '/api',
    paramsSerializer: params => qs.stringify(params, {arrayFormat: 'brackets'})
})

http.interceptors.request.use(params => {
    store.commit('setLoading', true)
    params.headers['Token'] = store.getters.getToken;
    return params
})

const STATUS_MESSAGE_MAP = {
    400: rs => rs.msg,
    500: "系统错误",
    401: "认证失败，请重新登录",
    403: "没有权限"
};

http.interceptors.response.use(
    response => {
        const rs = response.data;
        store.commit('setLoading', false)
        const messageFuncOrText = STATUS_MESSAGE_MAP[rs.code];
        if (rs.code === 200) {
            return rs;
        } else {
            if (typeof messageFuncOrText === 'function') {
                message.warn(messageFuncOrText(rs));
            } else if (messageFuncOrText) {
                message.error(messageFuncOrText);
            }
            if (rs.code === 401) {
                router.push("/login");
            }
            // 抛出错误或返回一个特殊值，表示响应不是成功的
            throw new Error(`Response failed with code ${rs.code}`);
        }
    },
    error => {
        store.commit('setLoading', false)
        message.error("网络错误")
        return Promise.reject(error);
    }
);



export default http
