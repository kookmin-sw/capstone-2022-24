module.exports = {
	pluginOptions: {
		quasar: {
			importStrategy: 'kebab',
			rtlSupport: false,
		},
	},
	transpileDependencies: ['quasar'],
	devServer: {
		public: process.env.VUE_APP_HOST || 'localhost',
		port: process.env.VUE_APP_PORT || 8080,
	},
};
