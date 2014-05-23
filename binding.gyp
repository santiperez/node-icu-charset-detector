{
  'targets': [
    {
      'target_name': 'node-icu-charset-detector',
      'sources': [ 'node-icu-charset-detector.cpp' ],
      'cflags!': [ '-fno-exceptions', '`icu-config --cppflags`' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'conditions': [
        ['OS=="mac"', {
          'include_dirs': [
              '/opt/local/include'
          ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          },
		  'libraries': ['`icu-config --ldflags`' ],
        }],
         ['OS=="linux"', {

		'libraries': ['`icu-config --ldflags`' ],
        }],
	['OS=="win"', {
          'include_dirs': [
              'C:\Program Files (x86)\icu\include'
          ],
          'libraries': [
            '-lC:\\Program Files (x86)\\icu\\lib\\*'			
          ]
        }]
      ]
    }
  ]
}
