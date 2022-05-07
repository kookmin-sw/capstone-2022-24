module.exports = {
	pluginOptions: {
		quasar: {
			importStrategy: 'kebab',
			rtlSupport: false,
		},
	},
	transpileDependencies: ['quasar'],
	devServer: {
		port: process.env.VUE_APP_PORT || 8080,
	},
};
