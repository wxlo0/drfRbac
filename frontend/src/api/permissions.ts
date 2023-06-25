import http from "@/utils/http";

export async function permissionsList() {
    return await http.get(`/user/permissions/list`)
}
