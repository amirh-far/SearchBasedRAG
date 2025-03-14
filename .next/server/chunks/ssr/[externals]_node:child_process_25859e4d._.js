module.exports = {

"[externals]/node:child_process [external] (node:child_process, cjs, async loader)": ((__turbopack_context__) => {

var { g: global, d: __dirname } = __turbopack_context__;
{
__turbopack_context__.v((parentImport) => {
    return Promise.all([
  "server/chunks/ssr/[externals]_node:child_process_f1e2641f._.js"
].map((chunk) => __turbopack_context__.l(chunk))).then(() => {
        return parentImport("[externals]/node:child_process [external] (node:child_process, cjs)");
    });
});
}}),

};