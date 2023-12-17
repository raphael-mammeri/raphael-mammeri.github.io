keyboard$.subscribe(function(key) {
    if (key.mode === "global" && key.type === "j") {
        KeyboardEvent.key("ArrowDown")
      key.claim() 
    }
  })