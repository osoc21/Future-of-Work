module.exports = {
  parserOptions: {
    ecmaVersion: 2020,
    sourceType: 'module'
  },
  env: {
    es6: true,
    browser: true,
    node: true
  },
  extends: ['eslint:recommended', 'prettier'],
  plugins: ['svelte3', 'prettier'],
  ignorePatterns: ['node_modules/'],
  overrides: [
    {
      files: ['**/*.svelte'],
      processor: 'svelte3/svelte3'
    }
  ],
  rules: {
    'comma-dangle': ['error', 'never'],
    'no-console': 'warn',
    'no-unused-expressions': ['error', { allowTernary: true }],
    'no-return-assign': [2, 'except-parens'],
    'no-param-reassign': ['error', { props: false }]
  }
};
